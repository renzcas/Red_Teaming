# world_model_integrator.py
from dataclasses import dataclass
from typing import Dict, Any
import time

from .cognitive_reactor import CognitiveEffect
from .worldnode import WorldNode
from .memory import Memory


@dataclass
class IntegrationResult:
    """Represents the outcome of integrating a cognitive effect."""
    status: str
    details: Dict[str, Any]
    timestamp: float


class WorldModelIntegrator:
    """
    Integrates cognitive effects into the world model and memory.
    This is the hippocampal consolidation organ.
    """

    def __init__(self, world: WorldNode, memory: Memory):
        self.world = world
        self.memory = memory

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def integrate(self, effect: CognitiveEffect) -> IntegrationResult:
        """
        Merge the cognitive effect into:
          - world model facts
          - hypotheses
          - contradictions
          - episodic memory
        """

        if effect.action.startswith("investigate_"):
            return self._integrate_investigation(effect)

        if effect.action.startswith("challenge_"):
            return self._integrate_challenge(effect)

        if effect.action == "generate_hypothesis":
            return self._integrate_hypothesis(effect)

        # fallback
        return IntegrationResult(
            status="ignored",
            details={"reason": "no integration rule"},
            timestamp=time.time()
        )

    # ---------------------------------------------------------
    # INTEGRATION RULES
    # ---------------------------------------------------------
    def _integrate_investigation(self, effect: CognitiveEffect) -> IntegrationResult:
        target = effect.target

        self.world.set_fact(
            f"investigation_active_{target}",
            True,
            confidence=0.9
        )

        self.memory.store_event(
            f"Integrated investigation for {target}",
            effect.details
        )

        return IntegrationResult(
            status="investigation_integrated",
            details={"target": target},
            timestamp=time.time()
        )

    def _integrate_challenge(self, effect: CognitiveEffect) -> IntegrationResult:
        target = effect.target

        self.world.set_fact(
            f"assumption_challenged_{target}",
            True,
            confidence=0.8
        )

        self.memory.store_event(
            f"Integrated assumption challenge for {target}",
            effect.details
        )

        return IntegrationResult(
            status="challenge_integrated",
            details={"target": target},
            timestamp=time.time()
        )

    def _integrate_hypothesis(self, effect: CognitiveEffect) -> IntegrationResult:
        hypothesis = effect.details.get("hypothesis", {})
        self.world.add_hypothesis(hypothesis)

        self.memory.store_event(
            f"Hypothesis integrated for {effect.target}",
            hypothesis
        )

        return IntegrationResult(
            status="hypothesis_integrated",
            details=hypothesis,
            timestamp=time.time()
        )
