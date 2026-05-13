from fastapi import FastAPI
from openai import OpenAI

from routers.router import app_router
from settings import Settings

app = FastAPI()
app.include_router(app_router)

settings = Settings()

@app.get("/")
def read_root():
    ai = OpenAI(base_url=settings.API_BASE_URL, api_key=settings.API_KEY.get_secret_value())
    request = ai.chat.completions.create(model=settings.MODEL_NAME, messages=[{"role": "user", "content": "Tell me a fun fact"}])
    response = request.choices[0].message.content
    return {"answer": response, "model": settings.MODEL_NAME.value}
