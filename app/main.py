import os
from app.routers import graphql, health
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.rq_config import rq_lifespan_end, rq_lifespan_start

load_dotenv(override=True, verbose=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    worker_processes = rq_lifespan_start()

    yield  # FastAPI runs during this phase

    rq_lifespan_end(worker_processes=worker_processes)


app = FastAPI(lifespan=lifespan)

# CORS middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
# app.include_router(auth.router)
app.include_router(graphql.router)
app.include_router(health.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        timeout_keep_alive=600,
        limit_max_requests=1000,
    )
