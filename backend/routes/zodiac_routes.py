# routes/zodiac_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from services.zodiac.zodiac import Zodiac

router = APIRouter(
    prefix="/zodiac",
    tags=["Zodiac"],
)

class BirthDataRequest(BaseModel):
    birth_date: str
    birth_time: Optional[str] = None
    location: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "birth_date": "1977-05-05",
                "birth_time": "05:45",
                "location": "St. Louis, MO"
            }
        }
    }

@router.get("/status")
def status():
    return {"status": "ok", "message": "Zodiac API is up and running"}

@router.post("/report")
def get_zodiac_report(data: BirthDataRequest):
    try:
        zodiac = Zodiac(
            birth_date=data.birth_date,
            birth_time=data.birth_time or "12:00",  # fallback if missing
            location=data.location
        )
        report = zodiac.get_report()
        return {
            "status": "success",
            "summary": report.get("zodiac_summary"),
            "core_traits": report.get("core_traits"),
            "planetary_positions": report.get("planetary_positions"),
            "flat_aspects": report.get("flat_aspects"),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
