from app import create_app
import pytest
from inverra.indexer import inverted_index, document_store

@pytest.fixture(autouse=True)
def reset_index():
    inverted_index.clear()
    document_store.clear()

def test_index():
    app = create_app()
    client = app.test_client()

    response = client.post('/api/index')
    assert response.status_code == 200
    data = response.get_json()
    assert "document_count" in data
    

def test_search():
    app = create_app()
    client = app.test_client()

    # First, index the corpus
    client.post('/api/index')

    # Now, perform a search
    response = client.get('/api/search?q=example')
    assert response.status_code == 200
    data = response.get_json()
    assert "results" in data


def test_stats():
    app = create_app()
    client = app.test_client()

    # First, index the corpus
    client.post('/api/index')
    # Now, get stats
    response = client.get('/api/stats')
    assert response.status_code == 200
    data = response.get_json()
    assert "vocab_size" in data
    assert "document_count" in data
    assert "index_size" in data


