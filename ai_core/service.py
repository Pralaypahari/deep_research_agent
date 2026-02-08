from ai_core.graph.research_graph import build_research_graph
# Build graph once (important for performance)
graph = build_research_graph()

def run_deep_research(query: str) -> dict:
    """
    Entry point for backend.
    Runs the research graph once and returns final state.
    """

    initial_state = {
        "query": query,
        "subtasks": [],
        "completed": {},
        "current_subtask": None,
        "search_results": [],
        "notes": [],
        "answers": {},
        "critique": {}
    }

    final_state = graph.invoke(initial_state)

    return {
        "query": query,
        "answers": final_state.get("answers", {})
    }