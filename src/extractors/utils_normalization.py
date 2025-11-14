thonpython
import re

def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        return text
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text