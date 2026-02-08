# ai_core/graph/nodes/reader_node.py

from ai_core.graph.state import ResearchState


def reader_node(state: ResearchState):
    from ai_core.agents.reader import read_sources

    notes = read_sources(
        state["search_results"],
        state["current_subtask"]
    )

    # Initialize notes if not present
    if "notes" not in state:
        state["notes"] = []

    # Append (DO NOT overwrite)
    state["notes"].extend(notes)

    return state

