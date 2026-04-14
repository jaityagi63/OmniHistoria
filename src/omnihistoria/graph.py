"""In-memory graph utilities used by the MVP ingestion and retrieval pipeline."""

from __future__ import annotations

from dataclasses import asdict

from .schema import Edge, Event, Source


class OmniGraph:
    """Simple graph store to bootstrap local development workflows."""

    def __init__(self) -> None:
        self.events: dict[str, Event] = {}
        self.sources: dict[str, Source] = {}
        self.edges: list[Edge] = []

    def add_event(self, event: Event) -> None:
        self.events[event.event_id] = event

    def add_source(self, source: Source) -> None:
        self.sources[source.source_id] = source

    def add_edge(self, edge: Edge) -> None:
        if edge.source not in self.events:
            raise KeyError(f"unknown edge source event: {edge.source}")
        if edge.target not in self.events:
            raise KeyError(f"unknown edge target event: {edge.target}")
        self.edges.append(edge)

    def events_in_period(self, start_year: int, end_year: int) -> list[Event]:
        return [
            event
            for event in self.events.values()
            if event.start_year <= end_year and (event.end_year or event.start_year) >= start_year
        ]

    def disputed_events(self) -> list[Event]:
        return [event for event in self.events.values() if len(event.narratives) > 1]

    def export_snapshot(self) -> dict[str, list[dict[str, object]]]:
        return {
            "events": [asdict(event) for event in self.events.values()],
            "sources": [asdict(source) for source in self.sources.values()],
            "edges": [asdict(edge) for edge in self.edges],
        }
