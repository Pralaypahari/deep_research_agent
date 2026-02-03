from ai_core.graph.state import ResearchState

def critic_node(state: ResearchState):
    from ai_core.agents.critic import critique

    verdict = critique(state["content"])
    state["critique"] = verdict
    state["retries"] += 1
    return state
