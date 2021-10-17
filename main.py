from fastapi import FastAPI, Request, status
from pydantic import BaseModel
import json
from typing import Optional
from collections import Counter

import spacy
from nltk.corpus import cess_esp
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/sentences")
def get_sentenses(text: str, lang: Optional[str] = 'es'):
    sp = spacy.load(f"{lang}_core_news_md")
    doc = sp(text)
    result = []
    for sent in doc.sents:
        result.append(sent.text)
    return {"output": result}


@app.post("/tokens")
def get_pos(sentence: str, lang: Optional[str] = 'es'):
    sp = spacy.load(f"{lang}_core_news_md")
    doc = sp(sentence)
    result = []
    for token in doc:
        #result.append([token, token.tag_, token.pos_, spacy.explain(token.tag_)])
        result.append([token.text, token.pos_, token.lemma_, token.dep_])
        #result.append("test")
    return {"output": result}

@app.post("/top")
def get_top(lang: Optional[str] = "es"):
    nlp = spacy.load(f'{lang}')
    doc = nlp(u'Your text here')

    words = [token.text
             for token in doc
             if not token.is_stop and not token.is_punct]

    # noun tokens that arent stop words or punctuations
    nouns = [token.text
             for token in doc
             if (not token.is_stop and
                 not token.is_punct and
                 token.pos_ == "NOUN")]

    # five most common tokens
    word_freq = Counter(words)
    common_words = word_freq.most_common(5)

    # five most common noun tokens
    noun_freq = Counter(nouns)
    common_nouns = noun_freq.most_common(5)
    return {"output": result}