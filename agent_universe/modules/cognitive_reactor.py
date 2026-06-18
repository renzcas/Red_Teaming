# cognitive_reactor.py
from dataclasses import dataclass
from typing import Callable, Dict, List
import time
from .planner_v3 import CognitiveAction
from .worldnode import WorldNode  # your world model
from .memory import Memory        # your memory system


@dataclass
class CognitiveEffect:
    """Result of executing a cognitive action."""
    action: str
    target: str
    details: Dict
    timestamp: float


class CognitiveReactor:
    """
    Executes internal cognitive actions selected by the Planner.
    This is the Motor Cortex of Thought.
    """

    def __init__(self, world: WorldNode, memory: Memory):
        self.world = world
        self.memory = memory

        # Map action names to handler functions
        self.handlers: Dict[str, Callable[[CognitiveAction], CognitiveEffect]] = {
            "investigate_signal": self._investigate_signal,
            "challenge_assumption": self._challenge_assumption,
            "generate_hypothesis": self._generate_hypothesis,
        }

    # ---------------------------------------------------------
    # MAIN EXECUTION ENTRY
    # ---------------------------------------------------------
    def execute(self, action: CognitiveAction) -> CognitiveEffect:
        handler = self.handlers.get(action.name)
        if not handler:
            return CognitiveEffect(
                action=action.name,
                target=action.target,
                details={"error": "unknown cognitive action"},
                timestamp=time.time()
            )
        return handler(action)

    # ---------------------------------------------------------
    # COGNITIVE ACTION IMPLEMENTATIONS
    # ---------------------------------------------------------
    def _investigate_signal(self, action: CognitiveAction) -> CognitiveEffect:
        # Mark the signal as "under investigation" in the world model
        self.world.set_fact(
            f"investigate_{action.target}",
            True,
            confidence=action.priority
        )

        self.memory.store_event(
            f"Investigating signal {action.target}",
            {"priority": action.priority}
        )

        return CognitiveEffect(
            action=action.name,
            target=action.target,
            details={"status": "investigation started"},
            timestamp=time.time()
        )

    def _challenge_assumption(self, action: CognitiveAction) -> CognitiveEffect:
        # Mark assumption as challenged
        self.world.set_fact(
            f"assumption_challenged_{action.target}",
            True,
            confidence=action.priority
        )

        self.memory.store_event(
            f"Challenged assumption about {action.target}",
            {"priority": action.priority}
        )

        return CognitiveEffect(
            action=action.name,
            target=action.target,
            details={"status": "assumption challenged"},
            timestamp=time.time()
        )

    def _generate_hypothesis(self, action: CognitiveAction) -> CognitiveEffect:
        hypothesis = {
            "target": action.target,
            "confidence": action.priority,
            "timestamp": time.time()
        }

        self.world.add_hypothesis(hypothesis)
        self.memory.store_event(
            f"Generated hypothesis for {action.target}",
            hypothesis
        )

        return CognitiveEffect(
            action=action.name,
            target=action.target,
            details={"hypothesis": hypothesis},
            timestamp=time.time()
        )
