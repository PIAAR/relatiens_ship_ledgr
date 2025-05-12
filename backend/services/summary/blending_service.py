# backend/services/summary/blending_service.py

from typing import Dict
from services.zodiac.zodiac_interpreter import ZodiacInterpreter
from services.zodiac.immanuel_engine import ImmanuelEngine


def get_zodiac_profile_summary(birth_date: str, birth_time: str, latitude: float, longitude: float) -> dict:
    zodiac_engine = ZodiacInterpreter()
    sky_engine = ImmanuelEngine(birth_date, birth_time, latitude, longitude)
    raw_chart = sky_engine.get_chart_objects()
    trait_summary = zodiac_engine.interpret_skyfield_chart(raw_chart)
    summary_text = zodiac_engine.summarize_relationship_profile(trait_summary)

    return {
        "sun": trait_summary.get("sun", {}).get("sign", "Unknown"),
        "summary": summary_text,
        "traits": trait_summary
    }


class SummaryBlender:
    def __init__(self, mbti: Dict, zodiac: Dict, human_design: Dict):
        self.mbti = mbti
        self.zodiac = zodiac
        self.human_design = human_design

    def blend(self) -> Dict:
        return {
            "mbti_type": self.mbti.get("type"),
            "zodiac_sun": self.zodiac.get("sun"),
            "human_design_type": self.human_design.get("type"),
            "compatibility_score": self._calculate_score(),
            "strongest_trait": self._strongest_trait(),
            "combined_summary": self._generate_summary()
        }

    def _generate_summary(self) -> str:
        return "\n".join([
            f"MBTI Insight: {self.mbti.get('summary', 'No MBTI summary available.')}",
            f"Zodiac Insight: {self.zodiac.get('summary', 'No Zodiac summary available.')}",
            f"Human Design Insight: {self.human_design.get('summary', 'No Human Design summary available.')}"
        ])

    def _strongest_trait(self) -> str:
        traits = self.mbti.get("trait_tags", [])
        return traits[0].capitalize() if traits else "Unknown"

    def _calculate_score(self) -> int:
        base_score = 100
        if self.mbti.get("type"): base_score += 20
        if self.zodiac.get("sun"): base_score += 20
        if self.human_design.get("type"): base_score += 20
        return min(base_score, 160)
