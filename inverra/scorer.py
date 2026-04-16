import math
from .indexer import inverted_index, document_store
from .tokeniser import tokenise

def compute_tf(term, doc_id):
    term_count = inverted_index[term][doc_id]
    total_tokens = document_store[doc_id]["token_count"]
    return term_count / total_tokens

def compute_idf(term):
    total_docs = len(document_store)
    docs_containing_term = len(inverted_index[term])
    return math.log(total_docs / (docs_containing_term + 1))  # Add 1 to avoid division by zero

def score(query_tokens, doc_id):
    total = 0.0
    for term in query_tokens:
        if term in inverted_index and doc_id in inverted_index[term]:
            tf = compute_tf(term, doc_id)
            idf = compute_idf(term)
            total += tf * idf
    return total

def search(query, top_k=10):
    query_tokens = tokenise(query)
    doc_scores = []
    for doc_id in document_store:
        doc_score = score(query_tokens, doc_id)
        if doc_score > 0:
            doc_scores.append((doc_id, doc_score))
    doc_scores.sort(key=lambda x: x[1], reverse=True)
    return doc_scores[:top_k]

