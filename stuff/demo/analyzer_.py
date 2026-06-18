# analyzer.py
from dataclasses import dataclass
from typing import Any, Dict, List
from parser import ParsedItem

@dataclass
class AnalysisDecision:
    label: str           # e.g. "normal", "suspicious", "error", "goal_trigger"
    score: float         # 0.0–1.0
    reasons: List[str]
    payload: Dict[str, Any]

class Analyzer:
    """
    The Analyzer is the reasoning organ.
    It takes ParsedItem and produces a decision.
    """

    def __init__(self):
        self.rules = []   # list of (name, fn)

    def register_rule(self, name: str, fn):
        """
        fn: (ParsedItem) -> List[AnalysisDecision]
        A rule can emit zero or more decisions.
        """
        self.rules.append((name, fn))

    def analyze(self, item: ParsedItem) -> List[AnalysisDecision]:
        decisions: List[AnalysisDecision] = []
        for name, fn in self.rules:
            try:
                out = fn(item)
                if out:
                    decisions.extend(out)
            except Exception as e:
                decisions.append(
                    AnalysisDecision(
                        label="analysis_error",
                        score=0.0,
                        reasons=[f"Rule {name} failed: {e}"],
                        payload={"item": item.data}
                    )
                )
        return decisions
