# backend/services/zodiac/immanuel_engine.py

from utils.immanuel import charts
from datetime import datetime

class ImmanuelEngine:
    def __init__(self, birth_date: str, birth_time: str, latitude: float, longitude: float):
        self.subject = charts.Subject(
            date_time=datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M"),
            latitude=latitude,
            longitude=longitude,
        )
        self.chart = charts.Natal(self.subject)

    def get_chart_objects(self) -> dict:
        return self.chart.objects

    def get_houses(self):
        return self.chart.houses

    def get_aspects(self):
        return self.chart.aspects
