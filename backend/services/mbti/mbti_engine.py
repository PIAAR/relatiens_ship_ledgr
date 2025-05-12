# services/mbti/mbti_engine.py

from services.mbti.question_bank import get_questions
from services.mbti.scoring_engine import score_mbti
from services.mbti.analyzer import cognitive_stack, get_summary
from models.mbti_result import MBTIResult
from db import mbti_collection
from datetime import datetime
from typing import List

def load_questions(version: int = 40):
    return get_questions(version)


def process_answers(user_id: str, answers: List[bool], version: int = 40) -> MBTIResult:
    questions = get_questions(version)
    mbti_type = score_mbti(questions, answers)
    summary = get_summary(mbti_type)
    functions = cognitive_stack(mbti_type)

    result = MBTIResult(
        user_id=user_id,
        mbti_type=mbti_type,
        cognitive_functions=functions,
        trait_tags=list(mbti_type),
        summary=summary,
        source="local",
        version=version,
        created_at=datetime.now().isoformat()
    )

    save_result(result)
    return result


def save_result(result: MBTIResult):
    mbti_collection.insert_one(result.dict())


def get_latest_result(user_id: str) -> MBTIResult:
    data = mbti_collection.find_one({"user_id": user_id}, sort=[("created_at", -1)])
    return MBTIResult(**data) if data else None


def get_all_results_for_user(user_id: str) -> List[dict]:
    return list(mbti_collection.find({"user_id": user_id}).sort("created_at", -1))


def analyze_mbti_type(mbti_type: str, user_id: str, source: str = "direct") -> MBTIResult:
    return MBTIResult(
        user_id=user_id,
        mbti_type=mbti_type,
        cognitive_functions=cognitive_stack(mbti_type),
        trait_tags=list(mbti_type),
        summary=get_summary(mbti_type),
        source=source,
        version=None,
        created_at=datetime.now().isoformat()
    )
