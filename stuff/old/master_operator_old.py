# master_operator.py
from dataclasses import dataclass
from typing import Dict, Any, Optional
import time

from .planner_v3 import CognitiveAction
from .cognitive_reactor import CognitiveEffect
from .world_model_integrator import IntegrationResult


@dataclass
class MetaDecision:
    """Represents a high-level executive decision."""
    action: str
    details: Dict[str, Any]
    timestamp: float


class MasterOperator:
    """
    The top-level executive organ.
    Oversees the entire cognitive cycle and ensures:
      - no infinite loops
      - no stagnation
      - mode switching
      - cognitive stability
      - global orchestration
    """

    def __init__(self):
        self.last_action: Optional[str] = None
        self.last_effect: Optional[str] = None
        self.loop_counter = 0
        self.mode = "default"

    # ---------------------------------------------------------
    # MAIN EXECUTIVE LOOP
    # ---------------------------------------------------------
    def supervise(
        self,
        action: CognitiveAction,
        effect: CognitiveEffect,
        integration: IntegrationResult
    ) -> MetaDecision:

        self.loop_counter += 1

        # Detect repeated actions (stagnation)
        if action.name == self.last_action:
            return self._redirect_due_to_stagnation(action)

        # Detect repeated effects (looping)
        if effect.action == self.last_effect:
            return self._redirect_due_to_loop(effect)

        # Normal operation
        self.last_action = action.name
        self.last_effect = effect.action

        return MetaDecision(
            action="continue",
            details={"mode": self.mode},
            timestamp=time.time()
        )

    # ---------------------------------------------------------
    # EXECUTIVE RESPONSES
    # ---------------------------------------------------------
    def _redirect_due_to_stagnation(self, action: CognitiveAction) -> MetaDecision:
        self.mode = "exploration"
        return MetaDecision(
            action="switch_mode",
            details={
                "reason": "stagnation detected",
                "new_mode": self.mode,
                "stuck_on": action.name
            },
            timestamp=time.time()
        )

    def _redirect_due_to_loop(self, effect: CognitiveEffect) -> MetaDecision:
        self.mode = "divergence"
        return MetaDecision(
            action="switch_mode",
            details={
                "reason": "loop detected",
                "new_mode": self.mode,
                "loop_on": effect.action
            },
            timestamp=time.time()
        )
