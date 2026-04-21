from flask import Blueprint, jsonify, request
from .indexer import build_index, load_corpus, inverted_index, document_store
from .scorer import search


bp = Blueprint('api', __name__)

@bp.route('/index', methods=['POST'])
def index_corpus():
    corpus_path = 'corpus'  # You can make this configurable
    corpus = load_corpus(corpus_path)
    build_index(corpus)
    return jsonify({"message": "Corpus indexed successfully", "document_count": len(document_store)}), 200


@bp.route('/search', methods=['GET'])
def search_query():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    results = search(query)
    return jsonify({"query": query, "results": results}), 200

@bp.route('/stats', methods=['GET'])
def find_stats():
    stats = {   
        'vocab_size': len(inverted_index),
        'document_count': len(document_store),
        'index_size': sum(len(postings) for postings in inverted_index.values())
    }
    return jsonify(stats), 200
