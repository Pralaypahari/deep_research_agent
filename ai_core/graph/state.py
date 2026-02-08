from typing import TypedDict, List, Dict

class ResearchState(TypedDict):
    query: str

    # Planning
    subtasks: list[str]
    completed: dict[str, bool]
    current_subtask: str | None

    # Research
    search_results: list[dict]
    notes: list[dict]        # <-- short-term memory

    answers: dict[str, str]
    # Critique
    critique: dict

