# redteam_cortex.py
from typing import List, Dict, Any


class RedTeamCortex:
    """
    Wraps all red-team brains into a unified cognitive layer.
    Each brain contributes:
      - hypotheses
      - contradictions
      - weak assumptions
      - adversarial signals
    """

    def __init__(self, brains: Dict[str, Any]):
        self.brains = brains

    def generate_cognitive_inputs(self, world) -> List[Dict[str, Any]]:
        signals = []

        for name, brain in self.brains.items():
            if hasattr(brain, "think"):
                out = brain.think(world)
                if out:
                    signals.extend(out)

        return signals
