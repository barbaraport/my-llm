from fastapi import APIRouter, Depends

from services.erasmus import Erasmus
from services.summarizer import Summarizer


erasmus_router = APIRouter(
    prefix="/erasmus",
    tags=["Erasmus"],
)

def get_service() -> Summarizer:
    return Erasmus()

@erasmus_router.get("/")
def erasmus_summarization(service: Summarizer = Depends(get_service)):
    return service.summarize("Erasmus summarization endpoint")