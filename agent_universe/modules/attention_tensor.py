# attention_tensor.py
from dataclasses import dataclass
from typing import Dict, List
import math
import time
from .order_parameter_engine import OrderParameter


@dataclass
class AttentionWeight:
    name: str
    weight: float
    timestamp: float


class AttentionTensor:
    """
    Takes OrderParameters and turns them into a normalized attention field.
    This is the cognitive spotlight: what the mind focuses on right now.
    """

    def __init__(self):
        self.weights: Dict[str, AttentionWeight] = {}

    def _softmax(self, values: Dict[str, float]) -> Dict[str, float]:
        if not values:
            return {}
        max_v = max(values.values())
        exps = {k: math.exp(v - max_v) for k, v in values.items()}
        s = sum(exps.values())
        return {k: (exps[k] / s) for k in exps}

    def update_from_order_parameters(
        self,
        ops: List[OrderParameter]
    ) -> Dict[str, AttentionWeight]:
        raw = {op.name: op.weight for op in ops}
        norm = self._softmax(raw)

        now = time.time()
        self.weights = {
            name: AttentionWeight(name=name, weight=w, timestamp=now)
            for name, w in norm.items()
        }
        return self.weights

    def top(self, n: int = 5) -> List[AttentionWeight]:
        return sorted(
            self.weights.values(),
            key=lambda x: x.weight,
            reverse=True
        )[:n]
