from ai_core.graph.state import ResearchState

def search_node(state: ResearchState):
    from ai_core.tools.search import search_web

    results = search_web(state["current_subtask"])

    state["search_results"] = results
    return state
