from core.summarizing.summarizer import Summarizer


class ErasmusSummarizer(Summarizer): 
    def summarize(self, content: str) -> str:
        return self.ai.prompt([{
            "role": "user",
            "content": f"Summarize the most important topics for Erasmus Mundus scholarships on this link: {content}"
        }])