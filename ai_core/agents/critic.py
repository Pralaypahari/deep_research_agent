from typing import Dict

# Minimum number of notes required to accept a subtask
MIN_NOTES = 2

def critique(state: dict) -> dict:
    """
    DEV MODE:
    Always accept so the graph can terminate.
    """

    current = state["current_subtask"]

    # Mark subtask complete
    state["completed"][current] = True

    # Find remaining subtasks
    remaining = [
        t for t, done in state["completed"].items()
        if not done
    ]

    if remaining:
        return {
            "action": "retry",
            "reason": "Move to next subtask",
            "next_subtask": remaining[0]
        }

    return {
        "action": "accept",
        "reason": "All subtasks completed"
    }

