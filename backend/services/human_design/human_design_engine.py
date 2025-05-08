# services/human_design/human_design_engine.py

from datetime import datetime
import logging
import httpx

logger = logging.getLogger(__name__)


class HumanDesignAPIClient:
    """
    Base interface for any Human Design API client.
    """

    def get_chart(self, birth_datetime, timezone):
        raise NotImplementedError("API client not implemented.")

    def get_composite_chart(self, date_a, timezone_a, date_b, timezone_b):
        raise NotImplementedError("Composite API client not implemented.")


class HumanDesignEngine:
    """
    Core engine for retrieving Human Design chart data.
    """

    def __init__(self, birth_date, birth_time, latitude, longitude, timezone, api_client=None):
        self.birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.api_client = api_client or HumanDesignAPIClient()

    def get_chart_data(self):
        try:
            chart_data = self.api_client.get_chart(
                self.birth_datetime,
                self.timezone
            )
            return chart_data
        except Exception as e:
            logger.error(f"Failed to fetch chart data: {e}")
            raise RuntimeError("Failed to retrieve Human Design chart data.") from e

    def get_composite_data(self, date_a, timezone_a, date_b, timezone_b):
        try:
            composite_data = self.api_client.get_composite_chart(
                date_a,
                timezone_a,
                date_b,
                timezone_b
            )
            return composite_data
        except Exception as e:
            logger.error(f"Failed to fetch composite chart data: {e}")
            raise RuntimeError("Failed to retrieve Human Design composite data.") from e
