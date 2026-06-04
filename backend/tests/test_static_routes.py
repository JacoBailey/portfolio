from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_homepage_endpoint_returns_html():
    response = client.get('/')
    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type']
    assert '<html' in response.text.lower()

def test_contact_endpoint_returns_html():
    response = client.get('/contact/')
    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type']
    assert '<html' in response.text.lower()

def test_projects_endpoint_returns_html():
    response = client.get('/projects/')
    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type']
    assert '<html' in response.text.lower()

def test_projects_chatgptautomation_endpoint_returns_html():
    response = client.get('/projects/chatgpt-automation/')
    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type']
    assert '<html' in response.text.lower()

def test_projects_formatter_endpoint_returns_html():
    response = client.get('/projects/text-formatter/')
    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type']
    assert '<html' in response.text.lower()

def test_projects_portfolio_endpoint_returns_html():
    response = client.get('/projects/portfolio/')
    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type']
    assert '<html' in response.text.lower()