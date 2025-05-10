# routes/mbti_routes.py

from fastapi import APIRouter, HTTPException
from services.mbti.clients.crystal_api_client import CrystalAPIClient
from services.mbti.mbti_engine import score_mbti_quiz, analyze_mbti_type

router = APIRouter()
crystal_client = CrystalAPIClient()

@router.get("/mbti/questions")
async def get_quiz_questions(premium: bool = False):
    if premium:
        return crystal_client.get_assessment_questions()
    else:
        # Return your local quiz from file or database
        return {"questions": [
            {"id": 1, "text": "Do you gain energy from being around people?", "dimension": "E/I"},
            {"id": 2, "text": "Do you focus more on facts or ideas?", "dimension": "S/N"},
            # Add more...
        ]}

@router.post("/mbti/analyze")
async def analyze_quiz(premium: bool, user_data: dict):
    if premium:
        crystal_profile = crystal_client.submit_assessment(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            responses=user_data["responses"]
        )
        return {
            "type": crystal_profile["personalities"]["myers_briggs_type"],
            "summary": crystal_profile["personalities"]["overview"],
            "details": crystal_profile["content"]
        }
    else:
        mbti_type = score_mbti_quiz(user_data["answers"])
        return analyze_mbti_type(mbti_type)
