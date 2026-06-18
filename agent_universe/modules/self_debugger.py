# self_debugger.py
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class DebugSignal:
    action: str
    details: Dict[str, Any]


class SelfDebugger:
    """
    Detects flawed cognitive patterns and corrects them.
    """

    def analyze(self, meta_memory, fatigue_state):
        # Too many contradictions → force consolidation
        contradictions = [
            e for e in meta_memory.events if e.event_type == "contradiction"
        ]
        if len(contradictions) > 5:
            return DebugSignal(
                action="force_mode",
                details={"new_mode": "consolidation", "reason": "contradiction_overload"}
            )

        # Too many entropy spikes → force focus
        entropy_spikes = [
            e for e in meta_memory.events if e.event_type == "entropy_spike"
        ]
        if len(entropy_spikes) > 4:
            return DebugSignal(
                action="force_mode",
                details={"new_mode": "focused", "reason": "entropy_overload"}
            )

        # Too many stagnation events → force exploration
        stagnation = [
            e for e in meta_memory.events if e.event_type == "stagnation"
        ]
        if len(stagnation) > 3:
            return DebugSignal(
                action="force_mode",
                details={"new_mode": "exploration", "reason": "stagnation_overload"}
            )

        # Fatigue too high → force idle
        if fatigue_state.fatigue > 0.9:
            return DebugSignal(
                action="force_mode",
                details={"new_mode": "idle", "reason": "fatigue_overload"}
            )

        return DebugSignal(action="none", details={})
