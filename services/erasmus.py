from services.base_service import BaseService


class ErasmusService(BaseService):
    def summarize(self) -> str:
        return self.summarizer.summarize("a test about erasmus mundus scholarships")