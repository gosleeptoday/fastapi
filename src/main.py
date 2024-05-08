from fastapi import FastAPI
from src.router import router
from src.database import init, shutdown
from fastapi.middleware.cors import CORSMiddleware

from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init()

@app.on_event("shutdown")
async def shutdown_event():
    await shutdown()

app = FastAPI(
    title="Phishing API",
    version="0.0.1",
    contact={"tg": "@evilnotlive"})

origins = [
    "http://127.0.0.1.tiangolo.com",
    "https://127.0.0.1.tiangolo.com",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

register_tortoise(
    app,
    db_url="sqlite://db.db",
    modules={"models": ["src.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)