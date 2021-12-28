from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from router.monolith import router
from router.api import api_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.router.include_router(router)
app.router.include_router(api_router)
