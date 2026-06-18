# master_operator.py
from dataclasses import dataclass
from typing import Dict, Any, Optional
import time

from .planner_v3 import CognitiveAction
from .cognitive_reactor import CognitiveEffect
from .world_model_integrator import IntegrationResult
from .meta_memory import MetaMemory
from .cognitive_fatigue import FatigueState
from .strategy_brain import Strategy
from .self_debugger import DebugSignal


@dataclass
class MetaDecision:
    """Represents a high-level executive decision."""
    action: str
    details: Dict[str, Any]
    timestamp: float


class MasterOperator:
    """
    The executive brain.
    Handles:
      - loop detection
      - stagnation detection
      - contradiction detection
      - entropy-based mode switching
      - fatigue-based suppression
      - meta-learning
      - self-debugging
      - long-term strategy influence
    """

    def __init__(self):
        self.last_action: Optional[str] = None
        self.last_effect: Optional[str] = None
        self.loop_counter = 0
        self.stagnation_counter = 0
        self.mode = "idle"

    # ---------------------------------------------------------
    # MAIN EXECUTIVE LOOP
    # ---------------------------------------------------------
    def supervise(
        self,
        action: CognitiveAction,
        effect: CognitiveEffect,
        integration: IntegrationResult,
        meta_memory: MetaMemory,
        fatigue_state: FatigueState,
        strategy: Strategy,
        debug_signal: DebugSignal
    ) -> MetaDecision:

        # -----------------------------------------------------
        # 1. SELF-DEBUGGING OVERRIDES EVERYTHING
        # -----------------------------------------------------
        if debug_signal.action == "force_mode":
            self.mode = debug_signal.details["new_mode"]
            return MetaDecision(
                action="switch_mode",
                details=debug_signal.details,
                timestamp=time.time()
            )

        # -----------------------------------------------------
        # 2. LOOP DETECTION
        # -----------------------------------------------------
        if action.name == self.last_action:
            self.stagnation_counter += 1
        else:
            self.stagnation_counter = 0

        if self.stagnation_counter >= 3:
            self.mode = "exploration"
            return MetaDecision(
                action="switch_mode",
                details={"reason": "stagnation_detected", "new_mode": self.mode},
                timestamp=time.time()
            )

        # -----------------------------------------------------
        # 3. EFFECT LOOP DETECTION
        # -----------------------------------------------------
        if effect.action == self.last_effect:
            self.mode = "divergence"
            return MetaDecision(
                action="switch_mode",
                details={"reason": "loop_detected", "new_mode": self.mode},
                timestamp=time.time()
            )

        # -----------------------------------------------------
        # 4. CONTRADICTION DETECTION
        # -----------------------------------------------------
        if "contradiction" in effect.type:
            self.mode = "consolidation"
            return MetaDecision(
                action="switch_mode",
                details={"reason": "contradiction_detected", "new_mode": self.mode},
                timestamp=time.time()
            )

        # -----------------------------------------------------
        # 5. ENTROPY-BASED MODE SWITCHING
        # -----------------------------------------------------
        entropy = fatigue_state.entropy

        if entropy > 0.85:
            self.mode = "consolidation"
            return MetaDecision(
                action="switch_mode",
                details={"reason": "entropy_high", "new_mode": self.mode},
                timestamp=time.time()
            )

        if 0.65 < entropy <= 0.85:
            self.mode = "divergence"
            return MetaDecision(
                action="switch_mode",
                details={"reason": "entropy_mid_high", "new_mode": self.mode},
                timestamp=time.time()
            )

        if 0.45 < entropy <= 0.65:
            self.mode = "exploration"
            return MetaDecision(
                action="switch_mode",
                details={"reason": "entropy_mid", "new_mode": self.mode},
                timestamp=time.time()
            )

        if entropy <= 0.45:
            self.mode = "focused"
            return MetaDecision(
                action="switch_mode",
                details={"reason": "entropy_low", "new_mode": self.mode},
                timestamp=time.time()
            )

        # -----------------------------------------------------
        # 6. META-LEARNING
        # -----------------------------------------------------
        meta_signal = self._meta_learning(meta_memory, fatigue_state)
        if meta_signal:
            self.mode = meta_signal["new_mode"]
            return MetaDecision(
                action="switch_mode",
                details=meta_signal,
                timestamp=time.time()
            )

        # -----------------------------------------------------
        # 7. STRATEGY INFLUENCE
        # -----------------------------------------------------
        if strategy.goal == "reduce_entropy" and entropy > 0.6:
            self.mode = "consolidation"
            return MetaDecision(
                action="switch_mode",
                details={"reason": "strategy_reduce_entropy", "new_mode": self.mode},
                timestamp=time.time()
            )

        if strategy.goal == "explore_unvisited_entities":
            self.mode = "exploration"
            return MetaDecision(
                action="switch_mode",
                details={"reason": "strategy_explore", "new_mode": self.mode},
                timestamp=time.time()
            )

        # -----------------------------------------------------
        # 8. NORMAL OPERATION
        # -----------------------------------------------------
        self.last_action = action.name
        self.last_effect = effect.action

        return MetaDecision(
            action="continue",
            details={"mode": self.mode},
            timestamp=time.time()
        )

    # ---------------------------------------------------------
    # META-LEARNING LOGIC
    # ---------------------------------------------------------
    def _meta_learning(self, meta_memory: MetaMemory, fatigue_state: FatigueState):
        last_mode = meta_memory.last_mode()
        last_entropy = meta_memory.last_entropy_spike()
        last_contradiction = meta_memory.last_contradiction()

        # Too many contradictions → consolidate
        if last_contradiction and fatigue_state.stability < 0.4:
            return {"new_mode": "consolidation", "reason": "meta_contradiction_history"}

        # Too many entropy spikes → focus
        if last_entropy and fatigue_state.entropy > 0.7:
            return {"new_mode": "focused", "reason": "meta_entropy_history"}

        # If last mode was exploration and fatigue is high → idle
        if last_mode == "exploration" and fatigue_state.fatigue > 0.6:
            return {"new_mode": "idle", "reason": "meta_fatigue_recovery"}

        return None
