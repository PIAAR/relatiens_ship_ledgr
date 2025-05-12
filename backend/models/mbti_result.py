# models/mbti_result.py

from pydantic import BaseModel
from typing import Optional

class MBTIResult(BaseModel):
    user_id: str
    mbti_type: str
    cognitive_functions: list[str]
    trait_tags: list[str]
    summary: str
    source: str
    version: int
    created_at: str
    crystal_profile: Optional[dict] = {}
