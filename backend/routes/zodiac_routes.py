# routes/zodiac_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Dict, Any
from services.zodiac.zodiac import Zodiac

router = APIRouter(
    prefix="/zodiac",
    tags=["Zodiac"],
)

# ----- Pydantic Request and Response Models -----

class BirthDataRequest(BaseModel):
    birth_date: str
    birth_time: Optional[str] = None
    location: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [{
                "birth_date": "1977-05-05",
                "birth_time": "05:45",
                "location": "St. Louis, MO"
            }]
        }
    )

class ZodiacReportData(BaseModel):
    summary: str
    core_traits: List[Any]
    planetary_positions: Dict[str, Any]
    flat_aspects: Dict[str, Any]

class ApiResponse(BaseModel):
    status: str
    data: ZodiacReportData
    message: str

# ----- API Endpoints -----

@router.get("/status")
def status():
    return {"status": "ok", "message": "Zodiac API is up and running"}

@router.post("/report", response_model=ApiResponse)
def get_zodiac_report(data: BirthDataRequest):
    try:
        zodiac = Zodiac(
            birth_date=data.birth_date,
            birth_time=data.birth_time or "12:00",
            location=data.location
        )
        report = zodiac.get_report()

        # Construct only the fields you want to expose in data
        zodiac_data = ZodiacReportData(
            summary=report.get("zodiac_summary"),
            core_traits=report.get("core_traits"),
            planetary_positions=report.get("planetary_positions"),
            flat_aspects=report.get("flat_aspects")
        )

        return ApiResponse(
            status="success",
            data=zodiac_data,
            message="Zodiac report generated successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
