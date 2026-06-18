# analyzer_v3.py
from dataclasses import dataclass
from typing import List, Dict, Any
import math
import time


@dataclass
class AnalyzerSignal:
    """Rich cognitive signal for the brain loop."""
    name: str
    value: float
    salience: float
    anomaly: float
    expectation_gap: float
    stability: float
    semantic_tags: List[str]
    metadata: Dict[str, Any]


class AnalyzerV3:
    """
    True cognitive analyzer.
    Converts raw observations into rich cognitive signals.
    """

    def __init__(self):
        self.last_values: Dict[str, float] = {}
        self.expectations: Dict[str, float] = {}

    # ---------------------------------------------------------
    # CORE FEATURE COMPUTATIONS
    # ---------------------------------------------------------
    def compute_salience(self, value: float) -> float:
        return abs(value)

    def compute_anomaly(self, value: float, expected: float) -> float:
        return abs(value - expected)

    def compute_stability(self, name: str, value: float) -> float:
        prev = self.last_values.get(name, value)
        self.last_values[name] = value
        return 1.0 / (1.0 + abs(value - prev))

    def compute_expectation_gap(self, name: str, value: float) -> float:
        expected = self.expectations.get(name, value)
        gap = abs(value - expected)
        self.expectations[name] = (expected * 0.8) + (value * 0.2)
        return gap

    def compute_semantic_tags(self, name: str, value: float) -> List[str]:
        tags = []
        if abs(value) > 0.7:
            tags.append("strong")
        if value < 0:
            tags.append("negative")
        if value > 0:
            tags.append("positive")
        if abs(value) < 0.2:
            tags.append("weak")
        return tags

    # ---------------------------------------------------------
    # MAIN ANALYSIS ENTRY
    # ---------------------------------------------------------
    def analyze(self, raw_inputs: Dict[str, float]) -> List[AnalyzerSignal]:
        signals = []

        for name, value in raw_inputs.items():
            expected = self.expectations.get(name, value)

            signal = AnalyzerSignal(
                name=name,
                value=value,
                salience=self.compute_salience(value),
                anomaly=self.compute_anomaly(value, expected),
                expectation_gap=self.compute_expectation_gap(name, value),
                stability=self.compute_stability(name, value),
                semantic_tags=self.compute_semantic_tags(name, value),
                metadata={
                    "timestamp": time.time(),
                    "expected": expected,
                }
            )

            signals.append(signal)

        return signals
