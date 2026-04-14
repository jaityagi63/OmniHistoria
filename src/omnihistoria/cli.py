"""CLI entry point for a lightweight local OmniHistoria MVP."""

from __future__ import annotations

import argparse
import json

from .graph import OmniGraph
from .prompts import build_conflict_prompt
from .schema import Edge, Event, Source


def seed_graph() -> OmniGraph:
    graph = OmniGraph()
    graph.add_source(Source("seshat-001", "Seshat Databank", "https://seshatdatabank.info", "dataset", 0.9))
    graph.add_source(Source("wiki-001", "Wikidata", "https://www.wikidata.org", "dataset", 0.7))

    graph.add_event(
        Event(
            event_id="event-french-revolution",
            name="French Revolution",
            start_year=1789,
            end_year=1799,
            region="Europe",
            narratives=[
                "A bourgeois revolution centered on class conflict.",
                "A broader social rupture driven by fiscal crisis and political legitimacy collapse.",
            ],
            source_ids=["seshat-001", "wiki-001"],
        )
    )
    graph.add_event(
        Event(
            event_id="event-haitian-revolution",
            name="Haitian Revolution",
            start_year=1791,
            end_year=1804,
            region="Caribbean",
            narratives=["A successful anti-slavery and anti-colonial revolution."],
            source_ids=["seshat-001"],
        )
    )

    graph.add_edge(Edge("event-french-revolution", "event-haitian-revolution", "influenced", 0.8))
    return graph


def main() -> None:
    parser = argparse.ArgumentParser(description="OmniHistoria MVP CLI")
    parser.add_argument("command", choices=["snapshot", "conflicts"], help="Action to run")
    args = parser.parse_args()

    graph = seed_graph()

    if args.command == "snapshot":
        print(json.dumps(graph.export_snapshot(), indent=2))
        return

    for event in graph.disputed_events():
        print(json.dumps(build_conflict_prompt(event), indent=2))


if __name__ == "__main__":
    main()
