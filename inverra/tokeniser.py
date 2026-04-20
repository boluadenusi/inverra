import re
import string

STOPWORDS = set([
    "a", "an", "the", "and", "or", "but", "if", "while", "with", "to", "of", "in", "on", "for", "by", "is", "are",])

def lowercase(text: str) -> str:
    return text.lower()

def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans("", "", string.punctuation))

def split_tokens(text: str) -> list:
    return text.split()

def remove_stopwords(tokens: list) -> list:
    return [token for token in tokens if token not in STOPWORDS]
     
def stem(token: str) -> str:
    for suffix in ["ing", "ed", "s"]:
        if token.endswith(suffix) and len(token) > len(suffix) + 2:
            return token[:-len(suffix)]
    return token

def tokenise(text: str) -> list:
    text = lowercase(text)
    text = remove_punctuation(text)
    tokens = split_tokens(text)
    tokens = [stem(token) for token in tokens]
    return remove_stopwords(tokens)
