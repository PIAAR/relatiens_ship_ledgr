# services/mbti/mbti_engine.py

from mbti import MBTI
from db import mbti_collection
from datetime import datetime

def score_mbti_quiz(answers: dict) -> str:
    """ Map answers to E/I, S/N, T/F, J/P counts and return MBTI type """
    return answers["E/I"] + answers["S/N"] + answers["T/F"] + answers["J/P"]

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
