# services/mbti/mbti_engine.py

from mbti.core import MBTI
from db import mbti_collection
from datetime import datetime

def get_quiz_questions(version: int = 40) -> list[dict]:
    mbti = MBTI(version=version)
    return mbti.questions

def score_mbti_quiz(responses: list[bool], version: int = 40) -> str:
    mbti = MBTI(version=version)
    mbti.answers = responses
    return mbti.result()["type"]

def analyze_mbti_type(mbti_type: str) -> dict:
    mbti_obj = MBTI(mbti_type)
    return {
        "type": mbti_type,
        "cognitive_functions": mbti_obj.functions,
        "trait_tags": list(mbti_obj.dichotomies.values()),
        "summary": f"{mbti_obj} is known for {mbti_obj.short_description}."
    }

def save_mbti_result(user_id: str, mbti_type: str, summary: str, source: str = "local", raw_data: dict = None):
    mbti_collection.insert_one({
        "user_id": user_id,
        "mbti_type": mbti_type,
        "summary": summary,
        "source": source,
        "crystal_profile": raw_data or {},
        "created_at": datetime.utcnow()
    })

def get_latest_mbti_result(user_id: str):
    return mbti_collection.find_one({"user_id": user_id}, sort=[("created_at", -1)])
