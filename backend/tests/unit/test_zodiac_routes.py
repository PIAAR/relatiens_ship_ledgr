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
    assert json_data["status"] == "success"
    assert "summary" in json_data
    assert "core_traits" in json_data
    assert "planetary_positions" in json_data
    assert "flat_aspects" in json_data
