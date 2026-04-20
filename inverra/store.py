import json
import os
from .indexer import inverted_index, document_store

def save_index(path):
    with open(path, 'w') as file:
        json.dump({"inverted_index": inverted_index, "document_store": document_store}, file)


def load_index(path):
    with open(path, 'r') as file:
        data = json.load(file)
        inverted_index.update(data["inverted_index"])
        document_store.update(data["document_store"])