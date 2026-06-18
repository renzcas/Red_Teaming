# planner_v3.py
from dataclasses import dataclass
from typing import List, Dict, Any
import time
from .attention_tensor import AttentionWeight


@dataclass
class CognitiveAction:
    """A high-level reasoning step the agent can take."""
    name: str
    target: str
    priority: float
    reasons: List[str]
    timestamp: float


class PlannerV3:
    """
    The Planner decides the next cognitive action based on:
      - attention weights
      - world model state
      - memory traces
      - internal goals
    """

    def __init__(self):
        self.goals: Dict[str, float] = {}  # goal_name -> weight

    # ---------------------------------------------------------
    # Register a goal with a baseline weight
    # ---------------------------------------------------------
    def register_goal(self, name: str, weight: float = 1.0):
        self.goals[name] = weight

    # ---------------------------------------------------------
    # Compute cognitive actions from attention
    # ---------------------------------------------------------
    def propose_actions(
        self,
        attention: List[AttentionWeight]
    ) -> List[CognitiveAction]:

        actions = []
        now = time.time()

        for att in attention:
            # Example mapping: attention → cognitive action
            actions.append(
                CognitiveAction(
                    name="investigate_signal",
                    target=att.name,
                    priority=att.weight,
                    reasons=[f"high attention on {att.name}"],
                    timestamp=now
                )
            )

            actions.append(
                CognitiveAction(
                    name="challenge_assumption",
                    target=att.name,
                    priority=att.weight * 0.8,
                    reasons=[f"potential weak assumption in {att.name}"],
                    timestamp=now
                )
            )

            actions.append(
                CognitiveAction(
                    name="generate_hypothesis",
                    target=att.name,
                    priority=att.weight * 0.6,
                    reasons=[f"novel pattern in {att.name}"],
                    timestamp=now
                )
            )

        return actions

    # ---------------------------------------------------------
    # Select the best action
    # ---------------------------------------------------------
    def select_action(self, actions: List[CognitiveAction]) -> CognitiveAction:
        return max(actions, key=lambda a: a.priority)
