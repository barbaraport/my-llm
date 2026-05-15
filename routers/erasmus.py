from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from core.ai.ai import AI
from core.summarizing.erasmus import ErasmusSummarizer
from services.base_service import BaseService
from services.erasmus import ErasmusService
from settings.get_setting import get_setting


erasmus_router = APIRouter(
    prefix="/erasmus",
    tags=["Erasmus"],
)

def get_service() -> BaseService:
    return ErasmusService(
        summarizer=ErasmusSummarizer(
            ai=AI(api_url=get_setting("API_BASE_URL"), 
                  api_key=get_setting("API_KEY"), 
                  model_name=get_setting("MODEL_NAME")
                )
            )
        )
    

@erasmus_router.get("/",
    summary="Summarize Erasmus scholarships",
    description="Fetches the Erasmus scholarships from the specified catalogue URL, summarizes them using an AI model, and returns the summary as a stream of markdown content.",
    response_description="A stream of markdown content summarizing the Erasmus scholarships.",
    response_class=StreamingResponse,
    responses={
        200: {
            "description": "Returns a continuous stream of text chunks (SSE - Server-Sent Events) that together form a markdown summary of the Erasmus scholarships.",
            "content": {"text/event-stream": {}}
        }
    }
)
def erasmus_summarization(service: BaseService = Depends(get_service)):
    stream = service.summarize()

    async def stream_wrapper():
        async for chunk in stream:
            yield chunk

    return StreamingResponse(
        stream_wrapper(),
        media_type="text/event-stream"
    )
