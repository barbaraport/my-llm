from fastapi import FastAPI

from routers.router import app_router

app = FastAPI()
app.include_router(app_router)
