# order_parameter_engine.py
from dataclasses import dataclass
from typing import Dict, Any, List
import math
import time


@dataclass
class Signal:
    """A normalized cognitive signal."""
    name: str
    value: float
    metadata: Dict[str, Any]


@dataclass
class OrderParameter:
    """Represents a computed priority/focus weight."""
    name: str
    weight: float
    reasons: List[str]
    timestamp: float


class OrderParameterEngine:
    """
    The cognitive organ that determines:
      - what is important
      - what is surprising
      - what is unstable
      - what deserves attention
    """

    def __init__(self):
        self.history: Dict[str, float] = {}  # last-seen values
        self.weights: Dict[str, OrderParameter] = {}

    # ---------------------------------------------------------
    # CORE: Compute salience from signal magnitude
    # ---------------------------------------------------------
    def compute_salience(self, signal: Signal) -> float:
        return abs(signal.value)

    # ---------------------------------------------------------
    # CORE: Compute surprise from change over time
    # ---------------------------------------------------------
    def compute_surprise(self, signal: Signal) -> float:
        prev = self.history.get(signal.name, None)
        self.history[signal.name] = signal.value

        if prev is None:
            return 0.0

        return abs(signal.value - prev)

    # ---------------------------------------------------------
    # CORE: Compute instability (variance-like)
    # ---------------------------------------------------------
    def compute_instability(self, signal: Signal) -> float:
        # instability = |value| * surprise
        surprise = self.compute_surprise(signal)
        return abs(signal.value) * surprise

    # ---------------------------------------------------------
    # CORE: Compute contradiction (signal vs metadata expectation)
    # ---------------------------------------------------------
    def compute_contradiction(self, signal: Signal) -> float:
        expected = signal.metadata.get("expected", None)
        if expected is None:
            return 0.0
        return abs(signal.value - expected)

    # ---------------------------------------------------------
    # MAIN: Compute order parameter weight
    # ---------------------------------------------------------
    def evaluate(self, signal: Signal) -> OrderParameter:
        salience = self.compute_salience(signal)
        surprise = self.compute_surprise(signal)
        instability = self.compute_instability(signal)
        contradiction = self.compute_contradiction(signal)

        # Weighted combination
        weight = (
            0.4 * salience +
            0.3 * surprise +
            0.2 * instability +
            0.1 * contradiction
        )

        reasons = []
        if salience > 0.5: reasons.append("high salience")
        if surprise > 0.3: reasons.append("unexpected change")
        if instability > 0.2: reasons.append("unstable signal")
        if contradiction > 0.2: reasons.append("contradiction detected")

        op = OrderParameter(
            name=signal.name,
            weight=weight,
            reasons=reasons,
            timestamp=time.time()
        )

        self.weights[signal.name] = op
        return op

    # ---------------------------------------------------------
    # Return top-N order parameters
    # ---------------------------------------------------------
    def top(self, n: int = 5) -> List[OrderParameter]:
        return sorted(
            self.weights.values(),
            key=lambda x: x.weight,
            reverse=True
        )[:n]
