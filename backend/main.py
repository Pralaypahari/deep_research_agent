from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.research import router as research_router

app = FastAPI(
    title="Deep Research Agent Backend",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(research_router, prefix="/research")

@app.get("/")
async def root():
    return {"status": "Backend running"}