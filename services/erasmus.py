from .summarizer import Summarizer


class Erasmus(Summarizer):
    def summarize(self, content: str) -> str:
        return f"Erasmus summary of: {content}"