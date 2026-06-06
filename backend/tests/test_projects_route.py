from fastapi.testclient import TestClient
from app.main import app
from app.schemas import ProjectRead

client = TestClient(app)

def test_projects_endpoint_returns_200():
    response = client.get('/api/projects/')
    assert response.status_code == 200

def test_projects_endpoint_returns_json_list():
    response = client.get('/api/projects/')
    data = response.json()
    assert response.headers["content-type"].startswith("application/json")
    assert isinstance(data, list)

def test_projects_endpoint_response_validates_against_schema():
    data = client.get('/api/projects/').json()
    for project in data:
        ProjectRead.model_validate(project)

def test_projects_endpoint_returns_bullets_in_order():
    data = client.get('/api/projects/').json()

    for project in data:
        bullets = project["bullets"]

        if len(bullets) < 2:
            continue

        for index in range(len(bullets) - 1):
            assert bullets[index]["order_index"] < bullets[index + 1]["order_index"]