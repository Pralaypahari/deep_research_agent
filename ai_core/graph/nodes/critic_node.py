from ai_core.graph.state import ResearchState

def critic_node(state: ResearchState):
    from ai_core.agents.critic import critique

    verdict = critique(state)
    state["critique"] = verdict

    if verdict["action"] == "retry":
        state["current_subtask"] = verdict["next_subtask"]

    return state


