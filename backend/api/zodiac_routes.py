from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.zodiac.zodiac import Zodiac

router = APIRouter()

class ZodiacRequest(BaseModel):
    birth_date: str
    location: str
    birth_time: str = "12:00"

@router.post("/profile")
def generate_profile(data: ZodiacRequest):
    try:
        zodiac = Zodiac(
            birth_date=data.birth_date,
            birth_time=data.birth_time,
            location=data.location
        )
        report = zodiac.get_report()
        core_traits = report["core_traits"]["core_traits"]
        interpreter = zodiac.interpreter

        insight = (
            f"With your Sun in {core_traits['sun']['sign']}, "
            f"you express yourself with {', '.join(core_traits['sun']['traits'][:2])}. "
            f"Your Moon in {core_traits['moon']['sign']} suggests emotional tendencies like "
            f"{', '.join(core_traits['moon']['traits'][:2])}. "
            f"Rising in {core_traits['asc']['sign']} shows you come off as "
            f"{', '.join(core_traits['asc']['traits'][:2])}."
        )

        return {
            "summary": report["zodiac_summary"],
            "core_traits": {
                key: {
                    "sign": value["sign"],
                    "traits": value["traits"][:2]
                }
                for key, value in core_traits.items() if key in ["sun", "moon", "asc"]
            },
            "relationship_insight": insight
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
