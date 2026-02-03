from ai_core.graph.state import ResearchState

def should_retry(state: ResearchState):
    if state["critique"]["action"] == "retry" and state["retries"] < 2:
        return "retry"
    return "accept"
