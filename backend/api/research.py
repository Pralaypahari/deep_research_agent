from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict
from ai_core.service import run_deep_research

router = APIRouter()


class ResearchRequest(BaseModel):
    query: str
    sources: List[str] | None = None


class ResearchResponse(BaseModel):
    query: str
    answers: Dict[str, str]




@router.get("/")
async def research_root():
    """
    Health check for research API
    """
    return {"status": "Research API running"}


@router.post("/query", response_model=ResearchResponse)
async def run_research(data: ResearchRequest):
    """
    Main research endpoint
    """
    result = run_deep_research(data.query)

    return {
        "query": result["query"],
        "answers": result["answers"]
    }