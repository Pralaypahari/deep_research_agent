from ai_core.graph.research_graph import build_research_graph
from ai_core.agents.planner import plan_tasks
from ai_core.memory.short_term import ShortTermMemory

def run_deep_research(query: str):
    tasks = plan_tasks(query)
    memory = ShortTermMemory()
    graph = build_research_graph()

    for task in tasks:
        state = {
            "task": task,
            "retries": 0
        }

        final_state = graph.invoke(state)
        memory.save(task, final_state["content"])

    return {
        "topic": query,
        "research": memory.get_all()
    }
