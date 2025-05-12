# backend/routes/profile_routes.py

from fastapi import APIRouter
from pydantic import BaseModel, Field
from services.profile.profile_db import save_full_profile
from services.summary.blending_service import get_zodiac_profile_summary

router = APIRouter(prefix="/profile", tags=["Profile"])

class ProfileSubmission(BaseModel):
    user_id: str
    mbti_type: str = Field(..., example="ENTJ")
    birth_date: str = Field(..., example="1977-05-05")
    birth_time: str = Field(..., example="05:45")
    latitude: float
    longitude: float

@router.post("/submit")
def submit_full_profile(data: ProfileSubmission):
    mbti = {
        "type": data.mbti_type,
        "summary": "Profile-based MBTI summary here.",
        "trait_tags": []  # Will enhance later
    }

    zodiac = get_zodiac_profile_summary(
        birth_date=data.birth_date,
        birth_time=data.birth_time,
        latitude=data.latitude,
        longitude=data.longitude
    )

    # Stub Human Design
    human_design = {
        "type": "Manifesting Generator",
        "summary": "Emotional authority with fast action potential."
    }

    save_full_profile(data.user_id, mbti=mbti, zodiac=zodiac, human_design=human_design)

    return {"status": "success", "message": "Profile saved."}
