from app import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_root_endpoint():
    client = app.test_client()
    response = client.get("/")
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["service"] == "smartgenie-sample"
    assert payload["status"] == "running"
