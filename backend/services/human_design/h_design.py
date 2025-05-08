# services/human_design/h_design.py

from services.human_design.human_design_engine import HumanDesignEngine
from services.human_design.human_design_interpreter import HumanDesignInterpreter
from utils.geocode import get_lat_long


class HumanDesign:
    """
    Orchestrates Human Design chart analysis.
    Calls the engine to get raw data and uses the interpreter to process it.
    """

    def __init__(self, birth_date, birth_time, latitude=None, longitude=None, location="Unknown", timezone="UTC", api_client=None):
        self.birth_date = birth_date
        self.birth_time = birth_time
        self.location = location
        self.timezone = timezone

        # Resolve latitude and longitude if not provided
        if latitude is None or longitude is None:
            self.latitude, self.longitude = get_lat_long(location)
        else:
            self.latitude = latitude
            self.longitude = longitude

        # Initialize engine and interpreter
        self.engine = HumanDesignEngine(
            birth_date, birth_time, self.latitude, self.longitude, self.timezone, api_client=api_client
        )
        self.interpreter = HumanDesignInterpreter()

        # Fetch chart data
        self._chart_data = self.engine.get_chart_data()

        # Process key attributes
        self._type = self.interpreter.get_type(self._chart_data)
        self._authority = self.interpreter.get_authority(self._chart_data)
        self._profile = self.interpreter.get_profile(self._chart_data)
        self._defined_centers = self.interpreter.get_defined_centers(self._chart_data)
        self._open_centers = self.interpreter.get_open_centers(self._chart_data)
        self._gates = self.interpreter.get_gates(self._chart_data)
        self._channels = self.interpreter.get_channels(self._chart_data)

    @property
    def summary(self):
        """
        Generate a human-friendly summary of the chart.
        """
        return self.interpreter.summarize_design(
            self._type,
            self._authority,
            self._profile,
            self._defined_centers,
            self._gates
        )

    def get_report(self) -> dict:
        """
        Return a structured report dictionary.
        """
        return {
            "birth_date": self.birth_date,
            "birth_time": self.birth_time,
            "location": self.location,
            "timezone": self.timezone,
            "type": self._type,
            "authority": self._authority,
            "profile": self._profile,
            "defined_centers": self._defined_centers,
            "open_centers": self._open_centers,
            "gates": self._gates,
            "channels": self._channels,
            "summary": self.summary
        }
