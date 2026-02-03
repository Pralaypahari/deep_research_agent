# ai_core/memory/short_term.py

class ShortTermMemory:
    def __init__(self):
        self.data = {}

    def save(self, task: str, content: dict):
        self.data[task] = content

    def get_all(self):
        return self.data
