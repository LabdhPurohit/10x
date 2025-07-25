from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_plan_wall():
    response = client.post("/plan/", json={
        "width": 2,
        "height": 2,
        "obstacles": [{"x": 0.5, "y": 0.5}]
    })
    assert response.status_code == 200
    assert "points" in response.json()

def test_get_trajectory():
    response = client.get("/trajectory/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
