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

    data = response.json()

    assert "duration_min" in data
    assert isinstance(data["duration_min"], float)


def test_predict_negative_distance():
    response = client.post(
        "/predict",
        json={
            "distance_km": -1,
            "passengers": 2,
            "hour_of_day": 14,
        },
    )

    assert response.status_code == 422


def test_predict_invalid_passengers():
    response = client.post(
        "/predict",
        json={
            "distance_km": 5,
            "passengers": 20,
            "hour_of_day": 14,
        },
    )

    assert response.status_code == 422


def test_predict_invalid_hour():
    response = client.post(
        "/predict",
        json={
            "distance_km": 5,
            "passengers": 2,
            "hour_of_day": 25,
        },
    )

    assert response.status_code == 422


def test_feedback():
    response = client.post(
        "/feedback",
        json={
            "request_id": "test-123",
            "actual_duration_min": 25.5,
        },
    )

    assert response.status_code == 200
    assert response.json() == {"status": "received"}
