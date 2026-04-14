import unittest

from omnihistoria import OmniGraph
from omnihistoria.prompts import build_conflict_prompt
from omnihistoria.schema import Edge, Event, Source


class GraphTests(unittest.TestCase):
    def test_period_and_dispute_queries(self):
        graph = OmniGraph()
        graph.add_source(Source("s1", "Source", "https://example.com", reliability=0.8))
        graph.add_event(
            Event(
                "e1",
                "Event One",
                100,
                120,
                narratives=["n1", "n2"],
                source_ids=["s1"],
            )
        )
        graph.add_event(Event("e2", "Event Two", 200, 210))
        graph.add_edge(Edge("e1", "e2", "influenced", 0.6))

        self.assertEqual(len(graph.events_in_period(110, 205)), 2)
        self.assertEqual(len(graph.disputed_events()), 1)

    def test_conflict_prompt_needs_two_narratives(self):
        with self.assertRaises(ValueError):
            build_conflict_prompt(Event("e1", "Single", 1900, narratives=["only one"]))


if __name__ == "__main__":
    unittest.main()
