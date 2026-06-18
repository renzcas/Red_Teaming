# world_model.py
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import time
import uuid


@dataclass
class WorldEvent:
    id: str
    timestamp: float
    source: str
    kind: str
    data: Dict[str, Any]


@dataclass
class WorldFact:
    key: str
    value: Any
    confidence: float
    last_updated: float


class WorldModel:
    """
    The WorldModel is the agent's internal representation of reality.
    It stores:
      - events (chronological)
      - facts (key-value beliefs)
      - entities (objects in the world)
      - memory (episodic traces)
    """

    def __init__(self):
        self.events: List[WorldEvent] = []
        self.facts: Dict[str, WorldFact] = {}
        self.entities: Dict[str, Dict[str, Any]] = {}
        self.episodic_memory: List[Dict[str, Any]] = []

    # -------------------------
    # EVENT SYSTEM
    # -------------------------
    def add_event(self, source: str, kind: str, data: Dict[str, Any]):
        event = WorldEvent(
            id=str(uuid.uuid4()),
            timestamp=time.time(),
            source=source,
            kind=kind,
            data=data
        )
        self.events.append(event)
        return event

    def recent_events(self, limit: int = 10):
        return self.events[-limit:]

    # -------------------------
    # FACT SYSTEM
    # -------------------------
    def set_fact(self, key: str, value: Any, confidence: float = 1.0):
        self.facts[key] = WorldFact(
            key=key,
            value=value,
            confidence=confidence,
            last_updated=time.time()
        )

    def get_fact(self, key: str) -> Optional[WorldFact]:
        return self.facts.get(key)

    def update_fact(self, key: str, value: Any, confidence: float = 1.0):
        if key in self.facts:
            self.facts[key].value = value
            self.facts[key].confidence = confidence
            self.facts[key].last_updated = time.time()
        else:
            self.set_fact(key, value, confidence)

    # -------------------------
    # ENTITY SYSTEM
    # -------------------------
    def register_entity(self, entity_id: str, attributes: Dict[str, Any]):
        self.entities[entity_id] = attributes

    def update_entity(self, entity_id: str, attributes: Dict[str, Any]):
        if entity_id not in self.entities:
            self.entities[entity_id] = {}
        self.entities[entity_id].update(attributes)

    def get_entity(self, entity_id: str):
        return self.entities.get(entity_id)

    # -------------------------
    # EPISODIC MEMORY
    # -------------------------
    def remember(self, info: Dict[str, Any]):
        self.episodic_memory.append({
            "timestamp": time.time(),
            "info": info
        })

    def recall_recent(self, limit: int = 5):
        return self.episodic_memory[-limit:]
