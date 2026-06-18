# reactor.py
from typing import Callable, Dict, List
from analyzer import AnalysisDecision

class Reactor:
    """
    The Reactor is the action organ.
    It maps decisions → actions (functions).
    """

    def __init__(self):
        # mapping: label -> list[callable]
        self.action_map: Dict[str, List[Callable[[AnalysisDecision], None]]] = {}

    def register_action(self, label: str, fn: Callable[[AnalysisDecision], None]):
        """
        When a decision with this label appears, fn will be called.
        """
        self.action_map.setdefault(label, []).append(fn)

    def react(self, decisions: List[AnalysisDecision]):
        for d in decisions:
            actions = self.action_map.get(d.label, [])
            if not actions:
                # no explicit action: could log or ignore
                continue
            for fn in actions:
                try:
                    fn(d)
                except Exception as e:
                    # minimal safe error handling
                    print(f"[Reactor] action for {d.label} failed: {e}")
