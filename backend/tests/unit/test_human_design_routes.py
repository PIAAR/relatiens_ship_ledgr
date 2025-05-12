# tests/unit/test_human_design_routes.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def mock_human_design(monkeypatch):
    class MockHumanDesign:
        def __init__(self, birth_date, birth_time, location, timezone=None):
            self.birth_date = birth_date
            self.birth_time = birth_time
            self.location = location
            self.timezone = timezone

        def get_report(self):
            return {
                "birth_date": "1990-01-01",
                "birth_time": "12:00:00",
                "location": "New York",
                "timezone": "America/New_York",
                "type": "Generator",
                "authority": "Emotional",
                "profile": "4/6",
                "centers": ["Sacral", "Root"],
                "gates": ["2", "3", "4"],
                "summary": "You are a Generator with Emotional authority and a 4/6 profile."
            }

    from services.human_design import h_design
    monkeypatch.setattr(h_design, "HumanDesign", MockHumanDesign)

def test_get_human_design_report_success(monkeypatch):
    response = client.post("/analysis/human-design/report", json={
        "birth_date": "1990-01-01",
        "birth_time": "12:00:00",
        "location": "New York",
        "timezone": "America/New_York"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "Generator"
    assert "summary" in data
    assert "defined_centers" in data

def test_get_human_design_report_validation_error():
    response = client.post("/analysis/human-design/report", json={
        "birth_date": "invalid-date",
        "birth_time": "12:00:00",
        "location": "New York",
        "timezone": "America/New_York"
    })
    assert response.status_code == 422

def test_get_human_design_report_missing_field():
    response = client.post("/analysis/human-design/report", json={
        "birth_date": "1990-01-01",
        "birth_time": "12:00:00"
    })
    assert response.status_code == 422
