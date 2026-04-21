# Inverra

A text search engine built from scratch in Python. 

Inverra implements the full search pipeline — tokenisation, an inverted index, TF-IDF ranking, disk persistence, and a REST API — using Python's standard library and Flask.

Built to demonstrate CS fundamentals: data structures, algorithms, and backend system design.

---

## How It Works

Inverra has three sequential pipelines:

**Ingestion** — `load_corpus()` walks the `corpus/` directory and reads every `.txt` file. Each file becomes one document. The filename is the document ID.

**Indexing** — Each document passes through the tokeniser: lowercased, punctuation stripped, stopwords removed, and basic suffix stemming applied. The resulting tokens are fed into an inverted index — a nested dict mapping every unique term to the documents it appears in and how many times. A document store maps each document ID to its metadata (title, raw text, token count) for snippet retrieval.

**Querying** — A search query passes through the same tokeniser as documents (critical for consistency). Each query term is looked up in the inverted index in O(1). Every candidate document is scored using TF-IDF:

```
TF  = occurrences of term in document / total tokens in document
IDF = log(total documents / documents containing term + 1)
score = sum of TF-IDF across all query terms
```

Results are sorted by score and the top-k are returned.

The built index is persisted to disk as JSON so it survives server restarts without rebuilding.

---

## Project Structure

```
inverra/
├── inverra/
│   ├── __init__.py
│   ├── tokeniser.py      # Lowercasing, punctuation removal, stopwords, stemming
│   ├── indexer.py        # Inverted index, document store, corpus loader
│   ├── scorer.py         # TF-IDF scoring and search
│   ├── store.py          # JSON serialisation and deserialisation of the index
│   └── api.py            # Flask Blueprint with three route handlers
├── corpus/               # .txt documents to be indexed
├── tests/
│   ├── test_tokeniser.py
│   ├── test_indexer.py
│   ├── test_scorer.py
│   ├── test_store.py
│   └── test_api.py
├── app.py                # Flask app factory and entry point
└── README.md
```

---

## Setup

**Clone the repo:**
```bash
git clone https://github.com/boluadenusi/inverra
cd inverra
```

**Create and activate a virtual environment:**
```bash
python -m venv env
source env/bin/activate        # macOS/Linux
env\Scripts\activate           # Windows
```

**Install dependencies:**
```bash
pip install flask pytest
```

**Add documents to the corpus:**

Drop any `.txt` files into the `corpus/` directory. Inverra ships with a sample corpus covering football, FC Barcelona, Lionel Messi, the 2022 World Cup, and Champions League history.

---

## Running the Server

```bash
python app.py
```

Server runs at `http://127.0.0.1:5000`.

---

## API Reference

### POST `/api/index`

Indexes all `.txt` files in the `corpus/` directory. Run this once before searching.

```bash
curl -X POST http://127.0.0.1:5000/api/index
```

**Response:**
```json
{
  "message": "Corpus indexed successfully",
  "document_count": 6
}
```

---

### GET `/api/search?q=<query>`

Returns documents ranked by TF-IDF relevance score.

```bash
curl "http://127.0.0.1:5000/api/search?q=messi%20barcelona"
```

**Response:**
```json
{
  "query": "messi barcelona",
  "results": [
    ["messi_career.txt", 0.0062332156168873375],
    ["barcelona_history.txt",  0.005259275676748691],
    ["champions_league.txt", 0.0037208480978358077],
    ["la_masia.txt", 0.0037208480978358077]
  ]
}
```

---

### GET `/api/stats`

Returns index statistics.

```bash
curl http://127.0.0.1:5000/api/stats
```

**Response:**
```json
{
   "document_count": 6,
    "index_size": 494,
    "vocab_size": 349
}
```

---

## Running Tests

```bash
python -m pytest
```

31 tests across all modules — tokeniser, indexer, scorer, persistence, and API routes.

---

## Key CS Concepts

**Inverted index** — the core data structure of every real search engine. Maps terms to the documents containing them. O(1) term lookup.

**TF-IDF** — a probabilistic relevance model. Terms that appear frequently in a document but rarely across the corpus score highest.

**Hash maps** — the inverted index is a nested Python dict. Constant-time lookups regardless of corpus size.

**Text normalisation** — tokenisation, stopword removal, and stemming ensure that "running", "runs", and "run" are treated as the same term in both documents and queries.

**Serialisation** — the index is persisted to disk as JSON and rehydrated on load, so the server doesn't rebuild from scratch on every restart.

**REST API design** — HTTP verbs, query parameters, and JSON responses following standard conventions.

---

## PS:

A note on IDF and corpus diversity — terms that appear across every document in the corpus ('football' here) score an IDF of zero and return no results. This is correct behaviour, not a bug. IDF measures how rare a term is across the corpus — a term in every document carries no discriminating power. In a diverse corpus spanning multiple topics, this behaviour resolves naturally.