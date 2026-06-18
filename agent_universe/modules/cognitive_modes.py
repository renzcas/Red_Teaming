# cognitive_modes.py
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class ModeProfile:
    """Defines how a cognitive mode shapes the mind."""
    name: str
    attention_bias: float
    exploration_bias: float
    contradiction_bias: float
    hypothesis_bias: float
    consolidation_bias: float
    description: str


class CognitiveModes:
    """
    Defines the mental states the agent can enter.
    These modes influence:
      - attention weighting
      - planner priorities
      - hypothesis generation
      - assumption challenging
      - world model updates
    """

    def __init__(self):
        self.modes: Dict[str, ModeProfile] = {
            "default": ModeProfile(
                name="default",
                attention_bias=1.0,
                exploration_bias=1.0,
                contradiction_bias=1.0,
                hypothesis_bias=1.0,
                consolidation_bias=1.0,
                description="Balanced cognitive state."
            ),

            "exploration": ModeProfile(
                name="exploration",
                attention_bias=0.8,
                exploration_bias=1.6,
                contradiction_bias=0.9,
                hypothesis_bias=1.4,
                consolidation_bias=0.7,
                description="Search widely for new patterns."
            ),

            "divergence": ModeProfile(
                name="divergence",
                attention_bias=0.6,
                exploration_bias=1.8,
                contradiction_bias=1.2,
                hypothesis_bias=1.7,
                consolidation_bias=0.5,
                description="Break out of loops by generating alternatives."
            ),

            "adversarial_focus": ModeProfile(
                name="adversarial_focus",
                attention_bias=1.4,
                exploration_bias=0.8,
                contradiction_bias=1.8,
                hypothesis_bias=1.2,
                consolidation_bias=1.0,
                description="Seek weak assumptions and contradictions."
            ),

            "consolidation": ModeProfile(
                name="consolidation",
                attention_bias=1.0,
                exploration_bias=0.5,
                contradiction_bias=0.8,
                hypothesis_bias=0.6,
                consolidation_bias=1.8,
                description="Stabilize and integrate knowledge."
            ),
        }

    def get(self, mode_name: str) -> ModeProfile:
        return self.modes.get(mode_name, self.modes["default"])
