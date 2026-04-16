import os
from .tokeniser import tokenise

inverted_index = {}
document_store = {}


def load_corpus(corpus_path):
    corpus = []
    for filename in os.listdir(corpus_path):
        full_path = os.path.join(corpus_path, filename)
        if not filename.endswith('.txt') or not os.path.isfile(full_path):
            continue
        with open(full_path, 'r', encoding='utf-8') as file:
            corpus.append((filename, file.read()))
    return corpus

def build_index(corpus):
    for doc_id, text in corpus:
        tokens = tokenise(text)
        document_store[doc_id] = {"title": doc_id, "raw_text": text, "token_count": len(tokens)}
        for token in tokens:
            if token not in inverted_index:
                inverted_index[token] = {}
            if doc_id not in inverted_index[token]:
                inverted_index[token][doc_id] = 0
            inverted_index[token][doc_id] += 1

def get_postings(term):
    return inverted_index.get(term, {})
        




