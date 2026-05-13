from abc import ABC, abstractmethod

from core.summarizing.summarizer import Summarizer


class BaseService(ABC):
    def __init__(self, summarizer: Summarizer):
        self.summarizer = summarizer
        super().__init__()

    @abstractmethod
    def summarize(self) -> str:
        ...