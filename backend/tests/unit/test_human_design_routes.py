# tests/unit/test_human_design_routes.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_human_design_report_success(monkeypatch):
    """
    Test a successful report response with mocked data.
    """

    # Mock HumanDesign.get_report to avoid live API call
    from services.human_design import h_design

    class MockHumanDesign:
        def get_report(self):
            return {
                "birth_date": "1990-01-01",
                "birth_time": "12:00:00",
                "location": "New York",
                "timezone": "America/New_York",
                "type": "Generator",
                "authority": "Emotional",
                "profile": "4/6",
                "defined_centers": ["Sacral", "Root"],
                "open_centers": ["Heart", "Head"],
                "gates": [2, 3, 4],
                "channels": ["2-14", "3-60"],
                "summary": "You are a Generator with Emotional authority and a 4/6 profile. Your defined centers are Sacral, Root. Key gates include 2, 3, 4."
            }

    monkeypatch.setattr(h_design, "HumanDesign", lambda *args, **kwargs: MockHumanDesign())

    response = client.post("/api/human-design/report", json={
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
    """
    Test API response to invalid request data.
    """

    response = client.post("/api/human-design/report", json={
        "birth_date": "invalid-date",
        "birth_time": "12:00:00",
        "location": "New York",
        "timezone": "America/New_York"
    })

    assert response.status_code == 422  # Pydantic validation error


def test_get_human_design_report_missing_field():
    """
    Test API response when required fields are missing.
    """

    response = client.post("/api/human-design/report", json={
        "birth_date": "1990-01-01",
        "birth_time": "12:00:00"
        # missing location, timezone
    })

    assert response.status_code == 422  # Pydantic validation error
