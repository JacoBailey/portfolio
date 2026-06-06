from fastapi.testclient import TestClient
from app.main import app
from app.schemas import TechnicalSkillRead

client = TestClient(app)

def test_skills_endpoint_returns_200():
    response = client.get('/api/skills/')
    assert response.status_code == 200

def test_skills_endpoint_returns_json_list():
    response = client.get('/api/skills/')
    data = response.json()
    assert response.headers["content-type"].startswith("application/json")
    assert isinstance(data, list)

def test_skills_endpoint_response_validates_against_schema():
    data = client.get('/api/skills/').json()
    for skill in data:
        TechnicalSkillRead.model_validate(skill)

def test_skills_endpoint_returns_bullets_in_order():
    data = client.get('/api/skills/').json()

    for skill in data:
        bullets = skill["bullets"]

        if len(bullets) < 2:
            continue

        for index in range(len(bullets) - 1):
            assert bullets[index]["order_index"] < bullets[index + 1]["order_index"]