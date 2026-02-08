from typing import List, Dict

def synthesize_answer(
    subtask: str,
    notes,
    llm
) -> str:
    """
    DEV MODE:
    Generate an answer directly without evidence constraints.
    """

    prompt = f"""
You are a knowledgeable research assistant.

Subtask:
{subtask}

Give a clear, helpful, and concise explanation.
"""

    response = llm.invoke(prompt)
    return response.content

