from typing import List, Dict

def read_sources(results: List[Dict], subtask: str) -> List[Dict]:
    """
    Convert search results into STRONG research notes.
    Each note must be a standalone factual statement.
    """

    notes = []

    for r in results:
        snippet = r.get("snippet", "").strip()
        link = r.get("link", "")

        if len(snippet) < 40:
            continue  # too weak

        note = {
            "subtask": subtask,
            "claim": snippet,
            "source": link,
        }

        notes.append(note)

    return notes

