# backend/services/zodiac/zodiac.py
import os
import json
from datetime import datetime
from immanuel import charts
from immanuel.classes.serialize import ToJSON

# Load standardized object name map (lowercase names only)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAP_PATH = os.path.join(BASE_DIR, "../../utils/immanuel/object_name_map.json")

with open(MAP_PATH) as f:
    _astro_name_data = json.load(f)
    VALID_NAMES = set(_astro_name_data["available_names"])

class Zodiac:
    def __init__(self, birth_date: str, birth_time: str, location: str, latitude: float, longitude: float):
        self.birth_date = birth_date
        self.birth_time = birth_time
        self.location = location
        self.latitude = latitude
        self.longitude = longitude

        self.chart = self._generate_chart()
        self.name_map = self._build_name_map()
        self.traits = self._extract_traits()
        self.summary = self._summarize_chart()

    def _generate_chart(self):
        subject = charts.Subject(
            date_time=datetime.strptime(f"{self.birth_date} {self.birth_time}", "%Y-%m-%d %H:%M"),
            latitude=self.latitude,
            longitude=self.longitude
        )
        return charts.Natal(subject)

    def _build_name_map(self):
        return {obj.name.strip().lower(): obj for obj in self.chart.objects.values()}

    def _safe_sign(self, name: str) -> str:
        obj = self.name_map.get(name.lower())
        return obj.sign.name if obj else "Unknown"

    def _extract_traits(self) -> dict:
        return {
            "core_traits": [
                f"Sun in {self._safe_sign('sun')}",
                f"Moon in {self._safe_sign('moon')}",
                f"Ascendant in {self._safe_sign('ascendant')}"
            ],
            "location": self.location
        }

    def _summarize_chart(self) -> str:
        sun = self._safe_sign("sun")
        moon = self._safe_sign("moon")
        ascendant = self._safe_sign("ascendant")
        return (
            f"Your chart reveals you're driven by qualities like {sun} (Sun), emotionally attuned as a {moon} Moon, "
            f"and outwardly express yourself as an {ascendant} Rising sign."
        )

    def get_report(self) -> dict:
        return {
            "birth_date": self.birth_date,
            "birth_time": self.birth_time,
            "location": self.location,
            "core_traits": self.traits["core_traits"],
            "zodiac_summary": self.summary,
            "planetary_positions": {
                obj.name: obj.sign.name for obj in self.chart.objects.values()
            },
            "houses": self.chart.houses,
            "aspects": self.chart.aspects,
        }

    def to_json(self) -> str:
        return json.dumps(self.chart, cls=ToJSON, indent=4)
