from inverra.indexer import build_index, get_postings, inverted_index, document_store
import pytest

@pytest.fixture(autouse=True)
def reset_index():
    inverted_index.clear()
    document_store.clear()

def test_build_index():
    corpus = [("doc1.txt", "python code python"), ("doc2.txt", "java code")]

    build_index(corpus)
    assert get_postings("python") == {"doc1.txt": 2}
    assert get_postings("code") == {"doc1.txt": 1, "doc2.txt": 1}
    assert get_postings("java") == {"doc2.txt": 1}

    assert document_store[("doc1.txt")] == {"title": "doc1.txt", "raw_text": "python code python", "token_count": 3}
    assert document_store[("doc2.txt")] == {"title": "doc2.txt", "raw_text": "java code", "token_count": 2}


def test_get_postings_nonexistent():
    corpus = [("doc1.txt", "python code python"), ("doc2.txt", "java code")]
    build_index(corpus)
    assert get_postings("ruby") == {}