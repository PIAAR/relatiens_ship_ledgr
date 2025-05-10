# routes/human_design_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import date, time
from services.human_design.h_design import HumanDesign
from services.human_design.clients.human_design_ai_client import HumanDesignAiAPIClient
from config import HUMANDESIGN_API_KEY  # Load from config.py

router = APIRouter(
    prefix="/human-design",
    tags=["Human Design"],
)

# ----- Pydantic Request and Response Models -----

from pydantic import ConfigDict

class HumanDesignRequest(BaseModel):
    birth_date: date = Field(...)
    birth_time: time = Field(...)
    location: str = Field(...)
    timezone: str = Field(...)

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{
                "birth_date": "1990-01-01",
                "birth_time": "12:00:00",
                "location": "New York",
                "timezone": "America/New_York"
            }]
        }
    )

class HumanDesignResponse(BaseModel):
    birth_date: date
    birth_time: time
    location: str
    timezone: str
    type: str
    authority: str
    profile: str
    defined_centers: list
    open_centers: list
    gates: list
    channels: list
    summary: str

# ----- Initialize API Client -----
api_client = HumanDesignAiAPIClient(HUMANDESIGN_API_KEY)


# ----- API Endpoints -----

@router.get("/status")
def get_api_status():
    return {
        "status": "ok",
        "message": "Human Design API is up and running",
        "monthly_limit": 1000,
        "calls_made": getattr(api_client, "call_count", 0),
        "calls_remaining": 1000 - getattr(api_client, "call_count", 0),
        "reset_date": "2025-06-07",
    }

@router.post("/report", response_model=HumanDesignResponse)
def get_human_design_report(request: HumanDesignRequest):
    try:
        hd = HumanDesign(
            birth_date=request.birth_date.strftime("%Y-%m-%d"),
            birth_time=request.birth_time.strftime("%H:%M"),
            location=request.location,
            timezone=request.timezone,
            api_client=api_client
        )
        return hd.get_report()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating Human Design report: {str(e)}")
