# routes/mbti_routes.py

from fastapi import APIRouter, HTTPException, Query, Path
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Union
from services.mbti.clients.crystal_api_client import CrystalAPIClient
from services.mbti.mbti_engine import (
    load_questions, process_answers, get_latest_result,
    get_all_results_for_user, analyze_mbti_type, MBTIResult
)

router = APIRouter(prefix="/mbti", tags=["MBTI"])
crystal_client = CrystalAPIClient()

# --- Request Models ---
class MBTILocalSubmission(BaseModel):
    user_id: str
    answers: List[bool]
    version: Optional[int] = 40

class MBTIPremiumSubmission(BaseModel):
    first_name: str
    last_name: str
    responses: List[dict]


# --- ROUTES ---

@router.get("/questions")
async def get_questions(
    premium: bool = Query(False),
    version: int = Query(40)
):
    if premium:
        return crystal_client.get_assessment_questions()
    return {"questions": load_questions(version)}

@router.post("/submit", response_model=MBTIResult)
async def submit_quiz(
    user_data: Union[MBTILocalSubmission, MBTIPremiumSubmission],
    premium: bool = Query(False)
):
    if premium:
        if not isinstance(user_data, MBTIPremiumSubmission):
            raise HTTPException(status_code=400, detail="Missing premium fields.")

        profile = crystal_client.submit_assessment(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            responses=user_data.responses
        )

        return MBTIResult(
            user_id=f"{user_data.first_name}.{user_data.last_name}".lower(),
            mbti_type=profile["personalities"]["myers_briggs_type"],
            cognitive_functions=[],
            trait_tags=[],
            summary=profile["personalities"]["overview"],
            source="crystal",
            crystal_profile=profile["content"],
            version=40,  # or whatever makes sense
            created_at=datetime.now().isoformat()
        )


    if not isinstance(user_data, MBTILocalSubmission):
        raise HTTPException(status_code=400, detail="Missing local quiz data.")

    return process_answers(
        user_id=user_data.user_id,
        answers=user_data.answers,
        version=user_data.version
    )

@router.get("/result/{user_id}", response_model=MBTIResult)
async def get_latest_mbti(user_id: str):
    result = get_latest_result(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="No result found.")
    return result


@router.get("/history/{user_id}")
async def get_all_results(user_id: str):
    return get_all_results_for_user(user_id)


@router.get("/analyze-type/{mbti_type}", response_model=MBTIResult)
async def analyze_known_type(
    mbti_type: str = Path(..., min_length=4, max_length=4),
    user_id: str = Query("anonymous")
):
    return analyze_mbti_type(mbti_type, user_id=user_id, source="direct")
