from langgraph.graph import StateGraph, END
from ai_core.graph.state import ResearchState

from ai_core.graph.nodes.search_node import search_node
from ai_core.graph.nodes.reader_node import reader_node
from ai_core.graph.nodes.critic_node import critic_node
from ai_core.graph.nodes.decision_node import should_retry
from ai_core.graph.nodes.planner_node import planner_node
from ai_core.graph.nodes.llm_node import synthesizer_node



def build_research_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("search", search_node)
    graph.add_node("read", reader_node)
    graph.add_node("critic", critic_node)
    graph.add_node("synthesis", synthesizer_node)

    graph.add_node("planner", planner_node)
    graph.set_entry_point("planner")
    graph.add_edge("planner", "search")


    graph.add_edge("search", "read")
    graph.add_edge("read", "synthesis")
    graph.add_edge("synthesis", "critic")

    graph.add_conditional_edges(
        "critic",
        should_retry,
        {
            "retry": "search",
            "accept": END
        }
    )

    return graph.compile()
