def plan_research(query: str) -> list[str]:
    """
    Breaks a research query into structured subtasks.
    """
    return [
        f"Definition and core idea of {query}",
        f"How {query} works",
        f"Benefits and strengths of {query}",
        f"Limitations and risks of {query}",
        f"Real-world applications of {query}",
        f"Future directions of {query}",
    ]
