# world_model_v2.py
from dataclasses import dataclass
from typing import Dict, List, Any
import time


@dataclass
class Entity:
    name: str
    attributes: Dict[str, Any]
    beliefs: Dict[str, float]


@dataclass
class Relation:
    source: str
    target: str
    type: str
    confidence: float
    metadata: Dict[str, Any]


class WorldModelV2:
    """
    Graph-based internal reality:
      - Entities (nodes)
      - Relations (edges)
      - Beliefs (confidence-weighted facts)
      - Hypotheses (proposed beliefs)
    """

    def __init__(self):
        self.entities: Dict[str, Entity] = {}
        self.relations: List[Relation] = []
        self.hypotheses: List[Dict[str, Any]] = []

    # ---------------------------
    # ENTITY MANAGEMENT
    # ---------------------------
    def ensure_entity(self, name: str):
        if name not in self.entities:
            self.entities[name] = Entity(
                name=name,
                attributes={},
                beliefs={}
            )

    def set_attribute(self, entity: str, key: str, value: Any):
        self.ensure_entity(entity)
        self.entities[entity].attributes[key] = value

    def set_belief(self, entity: str, belief: str, confidence: float):
        self.ensure_entity(entity)
        self.entities[entity].beliefs[belief] = confidence

    # ---------------------------
    # RELATIONS
    # ---------------------------
    def relate(self, source: str, target: str, type: str, confidence: float = 1.0):
        self.ensure_entity(source)
        self.ensure_entity(target)
        self.relations.append(
            Relation(
                source=source,
                target=target,
                type=type,
                confidence=confidence,
                metadata={"timestamp": time.time()}
            )
        )

    # ---------------------------
    # HYPOTHESES
    # ---------------------------
    def add_hypothesis(self, hypothesis: Dict[str, Any]):
        hypothesis["timestamp"] = time.time()
        self.hypotheses.append(hypothesis)
