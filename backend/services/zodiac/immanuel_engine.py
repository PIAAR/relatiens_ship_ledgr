# backend/services/zodiac/immanuel_engine.py

from utils.immanuel import charts
from datetime import datetime
from skyfield.api import utc


class ImmanuelEngine:
    def __init__(self, birth_date: str, birth_time: str, latitude: float, longitude: float):
        # Step 1: Create datetime and localize to UTC
        dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M").replace(tzinfo=utc)

        # Step 2: Create Subject
        self.subject = charts.Subject(
            date_time=dt,
            latitude=latitude,
            longitude=longitude,
        )

        # Step 3: Load Natal Chart
        self.chart = charts.Natal(self.subject)

    def get_chart_objects(self) -> dict:
        return self.chart.objects

    def get_houses(self):
        return self.chart.houses

    def get_aspects(self):
        return self.chart.aspects
