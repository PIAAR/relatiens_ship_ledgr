# backend/utils/immanuel/charts.py

from datetime import datetime
from skyfield.api import load, Topos
from dataclasses import dataclass


@dataclass
class Subject:
    date_time: datetime
    latitude: float
    longitude: float


class Natal:
    def __init__(self, subject: Subject):
        self.subject = subject
        self._load_data()
        self.objects = self._calculate_planets()
        self.houses = {}  # You can extend this later
        self.aspects = {}  # Optional, for angles

    def _load_data(self):
        self.ephemeris = load("de421.bsp")  # JPL ephemeris file
        self.ts = load.timescale()
        self.time = self.ts.from_datetime(self.subject.date_time)
        self.location = Topos(
            latitude_degrees=self.subject.latitude,
            longitude_degrees=self.subject.longitude,
        )

    def _calculate_planets(self):
        observer = self.ephemeris["earth"] + self.location
        sky = observer.at(self.time)
        planets = {
            "Sun": self.ephemeris["sun"],
            "Moon": self.ephemeris["moon"],
            "Mercury": self.ephemeris["mercury"],
            "Venus": self.ephemeris["venus"],
            "Mars": self.ephemeris["mars"],
            "Jupiter": self.ephemeris["jupiter barycenter"],
            "Saturn": self.ephemeris["saturn barycenter"],
        }

        results = {}
        for name, body in planets.items():
            astrometric = sky.observe(body)
            ra, dec, distance = astrometric.radec()
            results[name] = {
                "RA": ra.hours,
                "DEC": dec.degrees,
                "distance_au": distance.au,
            }
        return results
