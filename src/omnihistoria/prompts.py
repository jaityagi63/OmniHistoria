"""Prompt generation utilities for KG-SFT style fine-tuning examples."""

from __future__ import annotations

from .schema import Event


def build_conflict_prompt(event: Event) -> dict[str, str]:
    """Create a training example for contested historical events."""
    if len(event.narratives) < 2:
        raise ValueError("conflict prompt requires at least two narratives")

    user = (
        f"Provide a neutral analysis of '{event.name}' ({event.start_year}). "
        "Present competing narratives and explain why disagreement persists."
    )
    assistant = (
        f"Event: {event.name}\n"
        f"Region: {event.region}\n"
        "Competing narratives:\n"
        + "\n".join(f"- {narrative}" for narrative in event.narratives)
        + "\nMost evidenced reading: requires source-weighted scoring from citation graph."
    )

    return {"user": user, "assistant": assistant}


def build_timeline_prompt(events: list[Event], focus_region: str | None = None) -> dict[str, str]:
    """Create a timeline prompt sorted by start year."""
    ordered = sorted(events, key=lambda event: event.start_year)
    if focus_region:
        ordered = [event for event in ordered if event.region.lower() == focus_region.lower()]

    user = "Generate a concise, source-aware timeline from the provided events."
    assistant = "\n".join(f"- {event.start_year}: {event.name} ({event.region})" for event in ordered)
    return {"user": user, "assistant": assistant or "No events available for requested filter."}
