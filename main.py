from fastapi import FastAPI

from settings import Settings

app = FastAPI()
settings = Settings()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

