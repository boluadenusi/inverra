import re
import string

def lowercase(text: str) -> str:
    return text.lower()

def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans("", "", string.punctuation))

def split_tokens(text: str) -> list:
    return text.split()

def tokenise(text: str) -> list:
    text = lowercase(text)
    text = remove_punctuation(text)
    tokens = split_tokens(text)
    return tokens