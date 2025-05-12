# backend/routes/summary_routes.py

from fastapi import APIRouter, HTTPException
from services.summary.blending_service import SummaryBlender, get_zodiac_profile_summary
from services.profile.profile_db import save_full_profile, get_user_profile

router = APIRouter(
    tags=["Summary"]
)

@router.get("/summary/{user_id}", tags=["Summary"])
async def get_user_summary(user_id: str):
    """
    Returns the stored full-profile summary for the given user ID.
    """
    profile = get_user_profile(user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="No summary found for user.")

    mbti = profile.get("mbti", {})
    zodiac = profile.get("zodiac", {})
    human_design = profile.get("human_design", {})

    blender = SummaryBlender(mbti, zodiac, human_design)
    return blender.blend()


@router.post("/summary/{user_id}", tags=["Summary"])
async def generate_and_save_user_summary(user_id: str):
    """
    Simulates and saves a full-profile summary for the user.
    Replace mock data with dynamic inputs once front-end form is built.
    """

    # TODO: Replace with real logic based on submitted form/birth data
    mbti = {
        "type": "ENTJ",
        "summary": "You are a bold, strategic leader who thrives on challenge and efficiency.",
        "trait_tags": ["extroverted", "intuitive", "thinking", "judging"]
    }

    zodiac = get_zodiac_profile_summary(
        birth_date="1977-05-05",
        birth_time="05:45",
        latitude=38.623,
        longitude=-90.15
    )

    human_design = {
        "type": "Manifesting Generator",
        "summary": "You thrive by moving quickly toward aligned opportunities while respecting your emotional clarity."
    }

    # Save to MongoDB
    save_full_profile(user_id, mbti=mbti, zodiac=zodiac, human_design=human_design)

    # Return blended result
    blender = SummaryBlender(mbti, zodiac, human_design)
    return blender.blend()
