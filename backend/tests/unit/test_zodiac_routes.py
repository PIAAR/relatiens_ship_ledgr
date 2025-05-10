# tests/test_zodiac_routes.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_status_endpoint():
    response = client.get("/api/zodiac/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Zodiac API is up and running"}

def test_zodiac_report_success():
    payload = {
        "birth_date": "1977-05-05",
        "birth_time": "05:45",
        "location": "St. Louis, MO"
    }
    response = client.post("/api/zodiac/report", json=payload)
    assert response.status_code == 200
    json_data = response.json()

    # Check top-level keys
    assert json_data["status"] == "success"
    assert "data" in json_data
    assert "message" in json_data
    assert json_data["message"] == "Zodiac report generated successfully"

    # Check nested data keys
    data = json_data["data"]
    assert "summary" in data
    assert "core_traits" in data
    assert "planetary_positions" in data
    assert "flat_aspects" in data

    # Optionally: check types
    assert isinstance(data["summary"], str)
    assert isinstance(data["core_traits"], list)
    assert isinstance(data["planetary_positions"], dict)
    assert isinstance(data["flat_aspects"], dict)

# ----------------------- Optional Negative Tests ----------------------------#
def test_zodiac_report_missing_field():
    payload = {
        "birth_date": "1977-05-05",
        # "birth_time" is optional, but let's break location
        "location": ""
    }
    response = client.post("/api/zodiac/report", json=payload)
    assert response.status_code in (400, 422)  # depending on validation setup
