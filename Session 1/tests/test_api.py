from fastapi.testclient import TestClient

from src.api import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_predict_success():
    response = client.post(
        "/predict",
        json={
            "distance_km": 5.0,
            "passengers": 2,
            "hour_of_day": 14,
        },
    )

    assert response.status_code == 200
    assert "duration_min" in response.json()


def test_predict_negative_distance():
    response = client.post(
        "/predict",
        json={
            "distance_km": -1.0,
            "passengers": 1,
            "hour_of_day": 12,
        },
    )

    assert response.status_code == 422


def test_predict_invalid_passengers():
    response = client.post(
        "/predict",
        json={
            "distance_km": 5.0,
            "passengers": 20,
            "hour_of_day": 12,
        },
    )

    assert response.status_code == 422


def test_feedback():
    response = client.post(
        "/feedback",
        json={
            "request_id": "test-request",
            "actual_duration_min": 25.5,
        },
    )

    assert response.status_code == 200
    assert response.json() == {"status": "received"}