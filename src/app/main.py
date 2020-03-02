from app.api import movies, ping
from app.db import database, engine, metadata
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

metadata.create_all(engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8888"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
app.include_router(movies.router, prefix="/movies", tags=["movies"])
