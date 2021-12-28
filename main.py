from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .router import monolith
from .router import api

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.router.include_router(monolith.router)
app.router.include_router(api.router)
