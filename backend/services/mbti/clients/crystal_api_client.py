# services/mbti/clients/crystal_api_client.py

import httpx
import os

class CrystalAPIClient:
    def __init__(self):
        self.base_url = "https://api.crystalknows.com/v1"
        self.api_key = os.getenv("CRYSTAL_API_KEY")

    def get_assessment_questions(self):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = httpx.get(f"{self.base_url}/assessments/questions", headers=headers)
        response.raise_for_status()
        return response.json()["data"]

    def submit_assessment(self, first_name, last_name, responses):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"responses": responses}
        params = {"first_name": first_name, "last_name": last_name}
        response = httpx.post(f"{self.base_url}/assessments", headers=headers, params=params, json=payload)
        response.raise_for_status()
        return response.json()["data"]
