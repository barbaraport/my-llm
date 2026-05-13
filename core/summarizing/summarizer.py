from abc import ABC

from core.ai.ai import AI


class Summarizer(ABC):
    def __init__(self , ai: AI):
        self.ai = ai
    
    def summarize(self, content: str) -> str:
        return self.ai.prompt([{
            "role": "user",
            "content": f"Summarize the following content: {content}"
        }])