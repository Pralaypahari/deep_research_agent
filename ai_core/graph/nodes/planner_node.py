from ai_core.graph.state import ResearchState
from ai_core.agents.planner import plan_research

def planner_node(state: ResearchState):
    subtasks = plan_research(state["query"])

    state["subtasks"] = subtasks
    state["completed"] = {task: False for task in subtasks}
    state["current_subtask"] = subtasks[0]
    state["notes"] = []
    state["answers"] = {}

    return state
