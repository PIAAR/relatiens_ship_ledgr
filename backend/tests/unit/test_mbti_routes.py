def test_valid_mbti_input():
    response = client.post("/api/mbti/analyze", json={"mbti_type": "ENTP"})
    assert response.status_code == 200
    assert response.json()["type"] == "ENTP"

def test_invalid_mbti_input():
    response = client.post("/api/mbti/analyze", json={"mbti_type": "XYZ"})
    assert response.status_code == 400

def test_missing_mbti_input():
    response = client.post("/api/mbti/analyze", json={})
    assert response.status_code == 422  # Unprocessable Entity from FastAPI validation
