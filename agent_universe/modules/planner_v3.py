# planner_v3.py
from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class CognitiveAction:
    name: str
    target: str
    metadata: Dict[str, Any]


class PlannerV3:
    """
    Mode-aware planner with fatigue-based suppression.
    """

    def suppress_actions_due_to_fatigue(self, actions, fatigue_state):
        suppressed = []

        for a in actions:
            if fatigue_state.fatigue > 0.7:
                if a.name in ["explore_concept", "investigate_signal", "challenge_assumption"]:
                    continue

            if 0.5 < fatigue_state.fatigue <= 0.7:
                if a.name == "explore_concept":
                    continue

            suppressed.append(a)

        return suppressed if suppressed else actions

    def select_action(self, actions, mode_profile, fatigue_state):
        if not actions:
            return CognitiveAction("noop", "none", {})

        actions = self.suppress_actions_due_to_fatigue(actions, fatigue_state)

        # Mode-aware selection
        if mode_profile.name == "exploration":
            for a in actions:
                if a.name in ["explore_concept", "investigate_signal"]:
                    return a

        if mode_profile.name == "consolidation":
            for a in actions:
                if a.name == "challenge_assumption":
                    return a

        if mode_profile.name == "divergence":
            for a in actions:
                if a.name in ["explore_concept", "investigate_signal"]:
                    return a

        if mode_profile.name == "focused":
            target = actions[0].target
            for a in actions:
                if a.target == target:
                    return a

        if mode_profile.name == "idle":
            for a in actions:
                if a.metadata.get("reason") in ["anomaly_detected", "attack_path_detected"]:
                    return a
            return CognitiveAction("noop", "none", {})

        return actions[0]
