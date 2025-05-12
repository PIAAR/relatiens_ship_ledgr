# backend/services/zodiac/zodiac.py

from services.zodiac.immanuel_engine import ImmanuelEngine
from services.zodiac.zodiac_interpreter import ZodiacInterpreter
from utils.geocode import get_lat_long


class Zodiac:
    def __init__(self, birth_date, birth_time, latitude=None, longitude=None, location="Unknown"):
        self.birth_date = birth_date
        self.birth_time = birth_time
        self.location = location

        # If no coordinates provided, use geocode lookup
        if latitude is None or longitude is None:
            self.latitude, self.longitude = get_lat_long(location)
        else:
            self.latitude = latitude
            self.longitude = longitude

        # Skyfield engine for astronomical data
        self.engine = ImmanuelEngine(self.birth_date, self.birth_time, self.latitude, self.longitude)
        self.interpreter = ZodiacInterpreter()

        # Calculate chart and traits once on init
        self._chart_objects = self.engine.get_chart_objects()
        self._houses = self.engine.get_houses()
        self._aspects = self.engine.get_aspects()
        self._traits = self.interpreter.interpret_skyfield_chart(self._chart_objects)

    @property
    def traits(self) -> dict:
        return self._traits

    @property
    def summary(self) -> str:
        return self.interpreter.summarize_relationship_profile(self._traits)

    def get_report(self) -> dict:
        return {
            "birth_date": self.birth_date,
            "birth_time": self.birth_time,
            "location": self.location,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "planetary_positions": self._chart_objects,
            "houses": self._houses,
            "aspects": self.interpreter.unwrap_aspects(self._aspects),
            "flat_aspects": self.interpreter.summarize_aspects(self._aspects),
            "core_traits": self.traits,
            "zodiac_summary": self.summary
        }
