from ai_core.graph.state import ResearchState

def reader_node(state: ResearchState):
    from ai_core.agents.reader import read_sources

    content = read_sources(state["search_results"])
    state["content"] = content
    return state
