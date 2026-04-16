from inverra.tokeniser import lowercase, remove_punctuation, split_tokens, tokenise, stem
import pytest

def test_lowercase_uppercase():
    assert lowercase("MESSI") == "messi"

def test_lowercase_mixed():
    assert lowercase("FC Barcelona") == "fc barcelona"

def test_lowercase_lowercase():
    assert lowercase("messi") == "messi"

def test_lowercase_empty():
    assert lowercase("") == ""

def test_remove_punctuation_exclamation():
    assert remove_punctuation("goal!") == "goal"

def test_remove_punctuation_hyphen():
    assert remove_punctuation("goal-scoring") == "goalscoring"

def test_remove_punctuation_multiple():
    assert remove_punctuation("toooor!!!") == "toooor"

def test_remove_punctuation_none():
    assert remove_punctuation("messi scored") == "messi scored"

def test_remove_punctuation_empty():
    assert remove_punctuation("") == ""

def test_split_tokens_single():
    assert split_tokens("messi") == ["messi"]

def test_split_tokens_simple():
    assert split_tokens("messi scores") == ["messi", "scores"]

def test_split_tokens_multiple_spaces():
    assert split_tokens("messi   scores") == ["messi", "scores"]

def test_split_tokens_empty():
    assert split_tokens("") == []

def test_stem_ing():
    assert stem("scoring") == "scor"

def test_stem_ed():
    assert stem("scored") == "scor"

def test_stem_s():
    assert stem("goals") == "goal"

def test_tokenise_basic():
    assert tokenise("Mes que un club!!!") == ["mes", "que", "un", "club"]

def test_tokenise_numbers():
    assert tokenise("Messi has scored 900 goals") == ["messi", "has", "scor", "900", "goal"]

def test_tokenise_empty():
    assert tokenise("") == []

def test_tokenise_query_consistency():
    doc_tokens = tokenise("FC Barcelona is a football club based in Barcelona, Spain.")
    query_tokens = tokenise("What is FC Barcelona?")
    assert "fc" in doc_tokens
    assert "fc" in query_tokens
    assert "barcelona" in doc_tokens
    assert "barcelona" in query_tokens
    assert query_tokens == ["what", "is", "fc", "barcelona"]