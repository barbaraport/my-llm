from fastapi import APIRouter
from .erasmus import erasmus_router


app_router = APIRouter()
app_router.include_router(erasmus_router)