from fastapi.testclient import TestClient
from app.main import app
from app.schemas import ExperienceRead

client = TestClient(app)

def test_experience_endpoint_returns_200():
    response = client.get('/api/experience/')
    assert response.status_code == 200

def test_experience_endpoint_returns_json_list():
    response = client.get('/api/experience/')
    data = response.json()
    assert response.headers["content-type"].startswith("application/json")
    assert isinstance(data, list)

def test_experience_endpoint_response_validates_against_schema():
    data = client.get('/api/experience/').json()
    for experience in data:
        ExperienceRead.model_validate(experience)

def test_experience_endpoint_returns_bullets_in_order():
    data = client.get('/api/experience/').json()

    for experience in data:
        bullets = experience["bullets"]

        if len(bullets) < 2:
            continue

        for index in range(len(bullets) - 1):
            assert bullets[index]["order_index"] < bullets[index + 1]["order_index"]