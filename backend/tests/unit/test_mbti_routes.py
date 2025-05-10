import pytest
from fastapi.testclient import TestClient
from main import app  # assuming your FastAPI app is in main.py

client = TestClient(app)

def test_local_mbti_analysis():
    payload = {
        "premium": False,
        "user_data": {
            "answers": {"E/I": "I", "S/N": "N", "T/F": "F", "J/P": "J"}
        }
    }
    response = client.post("/mbti/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "INFJ"
    assert "cognitive_functions" in data

def test_premium_crystal_analysis(monkeypatch):
    # Mock CrystalAPIClient response
    class MockCrystalClient:
        def submit_assessment(self, first_name, last_name, responses):
            return {
                "personalities": {
                    "myers_briggs_type": "ENTP",
                    "overview": "Energetic and curious",
                },
                "content": {}
            }
    from services.mbti import mbti_routes
    mbti_routes.crystal_client = MockCrystalClient()

    payload = {
        "premium": True,
        "user_data": {
            "first_name": "Jane",
            "last_name": "Doe",
            "responses": [{"question_id": 1, "option_id": 2, "most_or_least": "most"}]
        }
    }
    response = client.post("/mbti/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "ENTP"
