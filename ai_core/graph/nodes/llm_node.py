from ai_core.graph.state import ResearchState
from ai_core.agents.llm_brain import synthesize_answer
from ai_core.llm import get_llm

def synthesizer_node(state: ResearchState):
    llm = get_llm()

    subtask = state["current_subtask"]
    answer = synthesize_answer(
        subtask=subtask,
        notes=state["notes"],
        llm=llm
    )

    state["answers"][subtask] = answer
    return state
