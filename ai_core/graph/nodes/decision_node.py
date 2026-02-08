from ai_core.graph.state import ResearchState

def should_retry(state: ResearchState):
    return state["critique"]["action"]
