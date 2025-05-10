# models/mbti_result.py
from pydantic import BaseModel
from typing import Optional

class MBTIResult(BaseModel):
    user_id: str
    mbti_type: str
    cognitive_functions: list[str]
    trait_tags: list[str]
    summary: str
    crystal_profile: Optional[dict]
    source: str  # 'local' or 'crystal'
