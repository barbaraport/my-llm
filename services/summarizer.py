from abc import ABC, abstractmethod


class Summarizer(ABC):
    @abstractmethod
    def summarize(self, content: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")