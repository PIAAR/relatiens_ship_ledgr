# services/human_design/clients/humandesign_ai_client.py

import httpx
from services.human_design.human_design_engine import HumanDesignAPIClient
from config import MAX_API_CALLS


class HumanDesignAiAPIClient(HumanDesignAPIClient):
    """
    API client for HumanDesign.ai.
    Tracks call count to enforce max API usage per month.
    """

    BASE_URL = "https://api.humandesign.ai"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.call_count = 0  # Tracks how many calls made this month

    def _increment_call(self):
        if self.call_count >= MAX_API_CALLS:
            raise RuntimeError(
                f"API call limit reached: {self.call_count}/{MAX_API_CALLS} calls this month."
            )
        self.call_count += 1

    def get_chart(self, birth_datetime, timezone):
        self._increment_call()
        url = f"{self.BASE_URL}/hd-data"
        params = {
            "date": birth_datetime.strftime("%Y-%m-%d %H:%M"),
            "timezone": timezone,
            "api_key": self.api_key
        }
        response = httpx.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        props = data.get("Properties", {})
        gates = [g["Option"] for g in props.get("Gates", {}).get("List", [])]
        channels = [c["Option"] for c in props.get("Channels", {}).get("List", [])]

        return {
            "type": props.get("Type", {}).get("Id"),
            "authority": props.get("InnerAuthority", {}).get("Id"),
            "profile": props.get("Profile", {}).get("Id"),
            "defined_centers": data.get("DefinedCenters", []),
            "open_centers": data.get("OpenCenters", []),
            "gates": gates,
            "channels": channels
        }

    def get_composite_chart(self, date_a, timezone_a, date_b, timezone_b):
        self._increment_call()
        url = f"{self.BASE_URL}/hd-data-composite"
        params = {
            "date": date_a.strftime("%Y-%m-%d %H:%M"),
            "timezone": timezone_a,
            "date1": date_b.strftime("%Y-%m-%d %H:%M"),
            "timezone1": timezone_b,
            "api_key": self.api_key
        }
        response = httpx.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        def extract_individual(data_part):
            props = data_part.get("Properties", {})
            gates = [g["Option"] for g in props.get("Gates", {}).get("List", [])]
            channels = [c["Option"] for c in props.get("Channels", {}).get("List", [])]
            return {
                "type": props.get("Type", {}).get("Id"),
                "authority": props.get("InnerAuthority", {}).get("Id"),
                "profile": props.get("Profile", {}).get("Id"),
                "defined_centers": data_part.get("DefinedCenters", []),
                "open_centers": data_part.get("OpenCenters", []),
                "gates": gates,
                "channels": channels
            }

        def extract_combined(data_part):
            props = data_part.get("Properties", {})
            relationship_channels = props.get("RelationshipChannels", {})
            connection_theme = props.get("ConnectionTheme", {}).get("Description", "")
            return {
                "defined_centers": data_part.get("DefinedCenters", []),
                "open_centers": data_part.get("OpenCenters", []),
                "definition": props.get("Definition", {}).get("Id"),
                "connection_theme": connection_theme,
                "relationship_channels": {
                    category: [
                        {
                            "option": ch["Option"],
                            "gates": ch["Gates"]
                        }
                        for ch in details["List"]
                    ]
                    for category, details in relationship_channels.items()
                }
            }

        return {
            "person_a": extract_individual(data.get("0", {})),
            "person_b": extract_individual(data.get("1", {})),
            "combined": extract_combined(data.get("Combined", {}))
        }
