# ai_core/agents/critic.py

def critique(content: dict) -> dict:
    score = 0.8 if len(content["summary"]) > 50 else 0.4

    return {
        "score": score,
        "action": "accept" if score > 0.6 else "retry"
    }
