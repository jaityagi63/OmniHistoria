"""Core schema objects for the OmniHistoria knowledge graph."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class EntityType(str, Enum):
    EVENT = "event"
    PERSON = "person"
    CIVILIZATION = "civilization"
    PLACE = "place"
    SOURCE = "source"


@dataclass(slots=True)
class Source:
    """A citation source used to support factual claims."""

    source_id: str
    title: str
    url: str
    source_type: str = "secondary"
    reliability: float = 0.5

    def __post_init__(self) -> None:
        if not self.source_id.strip():
            raise ValueError("source_id must not be empty")
        if not (0.0 <= self.reliability <= 1.0):
            raise ValueError("reliability must be between 0 and 1")


@dataclass(slots=True)
class Event:
    """Historical event node in the graph."""

    event_id: str
    name: str
    start_year: int
    end_year: int | None = None
    region: str = "global"
    narratives: list[str] = field(default_factory=list)
    source_ids: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.event_id.strip():
            raise ValueError("event_id must not be empty")
        if not self.name.strip():
            raise ValueError("name must not be empty")
        if self.end_year is not None and self.end_year < self.start_year:
            raise ValueError("end_year cannot be before start_year")


@dataclass(slots=True)
class Edge:
    """Relationship edge with evidence metadata."""

    source: str
    target: str
    relation: str
    evidence_strength: float = 0.5

    def __post_init__(self) -> None:
        if not self.relation.strip():
            raise ValueError("relation must not be empty")
        if not (0.0 <= self.evidence_strength <= 1.0):
            raise ValueError("evidence_strength must be between 0 and 1")
