import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test that the homepage loads correctly"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"DevOps Wisdom" in rv.data
