import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_local_mbti_analysis():
    response = client.post("/analysis/mbti/submit?premium=false", json={
        "user_id": "test_user",
        "answers": [True, False, True, False],
        "version": 4
    })

    assert response.status_code == 200
    data = response.json()
    assert "mbti_type" in data
    assert len(data["mbti_type"]) == 4
    assert "cognitive_functions" in data
    assert data["source"] == "local"

def test_premium_crystal_analysis(monkeypatch):
    class MockCrystalClient:
        def submit_assessment(self, first_name, last_name, responses):
            return {
                "personalities": {
                    "myers_briggs_type": "ENTP",
                    "overview": "Energetic and curious",
                },
                "content": {}
            }

    from routes import mbti_routes
    monkeypatch.setattr(mbti_routes, "crystal_client", MockCrystalClient())

    response = client.post("/analysis/mbti/submit?premium=true", json={
        "first_name": "Jane",
        "last_name": "Doe",
        "responses": [
            {"question_id": 1, "option_id": 2, "most_or_least": "most"}
        ]
    })

    assert response.status_code == 200
    data = response.json()
    assert data["mbti_type"] == "ENTP"
    assert data["source"] == "crystal"
