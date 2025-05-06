# backend/services/zodiac/zodiac.py

from services.zodiac.immanuel_engine import ImmanuelEngine
from utils.immanuel.zodiac_interpreter import ZodiacInterpreter
from utils.geocode import get_lat_long


class Zodiac:
    def __init__(self, birth_date, birth_time, latitude=None, longitude=None, location="Unknown"):
        self.birth_date = birth_date
        self.birth_time = birth_time
        self.location = location

        if latitude is None or longitude is None:
            self.latitude, self.longitude = get_lat_long(location)
        else:
            self.latitude = latitude
            self.longitude = longitude

        self.engine = ImmanuelEngine(self.birth_date, self.birth_time, self.latitude, self.longitude)
        self.interpreter = ZodiacInterpreter()

        self._chart_objects = self.engine.get_chart_objects()
        self._houses = self.engine.get_houses()
        self._aspects = self.engine.get_aspects()
        self._positions = self.interpreter.get_positions(self._chart_objects)
        self._traits = self.interpreter.interpret_chart(self._chart_objects)

    @property
    def traits(self):
        return {"core_traits": self._traits}

    @property
    def summary(self):
        def label(sign): return sign.capitalize() if sign else "Unknown"

        sun_sign = self._traits.get("sun", {}).get("sign")
        moon_sign = self._traits.get("moon", {}).get("sign")
        asc_sign = self._traits.get("asc", {}).get("sign")

        return f"Sun in {label(sun_sign)}, Moon in {label(moon_sign)}, Rising in {label(asc_sign)}."

    def get_report(self) -> dict:
        return {
            "birth_date": self.birth_date,
            "birth_time": self.birth_time,
            "location": self.location,
            "planetary_positions": self._positions,
            "houses": self._houses,
            "aspects": self.interpreter.unwrap_aspects(self._aspects),
            "flat_aspects": self.interpreter.summarize_aspects(self._aspects),
            "core_traits": self.traits,
            "zodiac_summary": self.summary
        }