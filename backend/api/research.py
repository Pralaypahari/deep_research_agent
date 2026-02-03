from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class ResearchRequest(BaseModel):
    query: str
    sources: List[str] | None = None


class ResearchResponse(BaseModel):
    query: str
    summary: str
    sources_used: List[str]



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
    summary = f"Research summary for: {data.query}"

    sources_used = data.sources if data.sources else ["google", "wikipedia"]

    return ResearchResponse(
        query=data.query,
        summary=summary,
        sources_used=sources_used
    )