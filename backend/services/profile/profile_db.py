# backend/services/profile/profile_db.py

from db import user_profile_collection
from datetime import datetime
from typing import Optional

def save_full_profile(user_id: str, mbti: dict = None, zodiac: dict = None, human_design: dict = None) -> str:
    """
    Upserts a complete or partial user profile with MBTI, Zodiac, and Human Design.
    Only non-null sections will be updated.
    """
    updates = {"timestamp": datetime.now()}
    if mbti: updates["mbti"] = mbti
    if zodiac: updates["zodiac"] = zodiac
    if human_design: updates["human_design"] = human_design

    result = user_profile_collection.update_one(
        {"user_id": user_id},
        {"$set": updates},
        upsert=True
    )

    return str(result.upserted_id) if result.upserted_id else "updated"

def get_user_profile(user_id: str) -> Optional[dict]:
    """
    Retrieves the full analysis profile for a user.
    """
    profile = user_profile_collection.find_one({"user_id": user_id})
    return profile or None
