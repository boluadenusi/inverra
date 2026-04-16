from inverra.scorer import compute_idf, compute_tf, score, search
from inverra.indexer import build_index, inverted_index, document_store
import math
import pytest

@pytest.fixture(autouse=True)
def reset_index():
    inverted_index.clear()
    document_store.clear()

def test_compute_tf():
    corpus = [("doc1.txt", "python code python"), ("doc2.txt", "java code"), ("doc3.txt", "python java search")]
    build_index(corpus)
    assert compute_tf("search", "doc3.txt") == 1 / 3

def test_compute_idf():
    corpus = [("doc1.txt", "python code python"), ("doc2.txt", "java code"), ("doc3.txt", "python java search")]
    build_index(corpus)
    assert compute_idf("search") == math.log(3 / (1 + 1))   # Only doc3 contain "search"

def test_score():
    corpus = [("doc1.txt", "python code python"), ("doc2.txt", "java code"), ("doc3.txt", "python java search")]
    build_index(corpus)
    assert score(["search"], "doc3.txt") == (1 / 3) * math.log(3 / (1 + 1))  # Example value

def test_search():
    corpus = [("doc1.txt", "python code python"), ("doc2.txt", "java code"), ("doc3.txt", "python java search")]
    build_index(corpus)
    assert search("search", top_k=1) == [("doc3.txt", 1 / 3 * math.log(3 / (1 + 1)))]  # Example value