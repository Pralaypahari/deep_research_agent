from langgraph.graph import StateGraph, END
from ai_core.graph.state import ResearchState

from ai_core.graph.nodes import (
    search_node,
    reader_node,
    critic_node,
    should_retry
)

def build_research_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("search", search_node)
    graph.add_node("read", reader_node)
    graph.add_node("critic", critic_node)

    graph.set_entry_point("search")

    graph.add_edge("search", "read")
    graph.add_edge("read", "critic")

    graph.add_conditional_edges(
        "critic",
        should_retry,
        {
            "retry": "search",
            "accept": END
        }
    )

    return graph.compile()
