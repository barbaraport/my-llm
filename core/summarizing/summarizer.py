from abc import ABC, abstractmethod
from typing import AsyncGenerator

from core.ai.ai import AI


class Summarizer(ABC):
    def __init__(self , ai: AI):
        self.ai = ai
    
    @abstractmethod
    def summarize(self, content: str) -> AsyncGenerator[str, None]:
        pass