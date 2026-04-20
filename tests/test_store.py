from inverra.store import save_index, load_index
from inverra.indexer import inverted_index, document_store, build_index
import pytest

@pytest.fixture(autouse=True)
def reset_index():
    inverted_index.clear()
    document_store.clear()

def test_save_index(tmp_path):
    corpus = [("doc1.txt", "python code python"), ("doc2.txt", "java code"), ("doc3.txt", "python java search")]
    build_index(corpus)
    path = tmp_path / "index.json"
    save_index(path)
    assert path.exists()


def test_load_index(tmp_path):
    corpus = [("doc1.txt", "python code python"), ("doc2.txt", "java code"), ("doc3.txt", "python java search")]
    build_index(corpus)
    path = tmp_path / "index.json"
    save_index(path)

    # Clear current index
    inverted_index.clear()
    document_store.clear()

    load_index(path)
    assert "python" in inverted_index  
    assert "doc1.txt" in document_store  
    