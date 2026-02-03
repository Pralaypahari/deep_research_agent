from typing import TypedDict, List, Dict

class ResearchState(TypedDict):
    task: str
    search_results: List[Dict]
    content: Dict
    critique: Dict
    retries: int
