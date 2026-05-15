import spacy
import re

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s+#.]', ' ', text)

    doc = nlp(text)

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct and len(token.text) > 2
    ]

    return " ".join(tokens)

