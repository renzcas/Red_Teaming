# strategy_brain.py
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Strategy:
    goal: str
    reason: str
    metadata: Dict[str, Any]


class StrategyBrain:
    """
    Forms long-term goals based on world-model structure and meta-memory.
    """

    def form_strategy(self, world, meta_memory, reward_signal):
        # If contradictions accumulate → goal: stabilize
        contradictions = [
            e for e in meta_memory.events if e.event_type == "contradiction"
        ]
        if len(contradictions) > 3:
            return Strategy(
                goal="stabilize_world_model",
                reason="too_many_contradictions",
                metadata={}
            )

        # If entropy spikes → goal: reduce chaos
        entropy_spikes = [
            e for e in meta_memory.events if e.event_type == "entropy_spike"
        ]
        if len(entropy_spikes) > 2:
            return Strategy(
                goal="reduce_entropy",
                reason="entropy_spike_history",
                metadata={}
            )

        # If reward is positive → reinforce exploration
        if reward_signal.reward > 0:
            return Strategy(
                goal="continue_exploration",
                reason="positive_reward",
                metadata={}
            )

        # If stagnation → goal: explore new nodes
        stagnation = [
            e for e in meta_memory.events if e.event_type == "stagnation"
        ]
        if stagnation:
            return Strategy(
                goal="explore_unvisited_entities",
                reason="stagnation_detected",
                metadata={}
            )

        # Default: maintain stability
        return Strategy(
            goal="maintain_stability",
            reason="default",
            metadata={}
        )
