# ai_core/agents/reader.py

def read_sources(results: list[dict]) -> dict:
    summaries = []
    key_points = []

    for r in results:
        summaries.append(r.get("snippet", ""))
        key_points.append(r.get("title", ""))

    return {
        "summary": " ".join(summaries),
        "key_points": key_points
    }
