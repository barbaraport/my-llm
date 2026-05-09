from fastapi import FastAPI
from openai import OpenAI

from settings import Settings

app = FastAPI()
settings = Settings()


@app.get("/")
def read_root():
    ai = OpenAI(base_url=settings.API_BASE_URL, api_key=settings.API_KEY.get_secret_value())
    request = ai.chat.completions.create(model="llama3.2", messages=[{"role": "user", "content": "Tell me a fun fact"}])
    response = request.choices[0].message.content
    return {"response": response}
