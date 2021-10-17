import spacy

sp = spacy.load(f"es_core_news_md")

# words = [token.text
#          for token in sp.vocab
#          if not token.is_stop and not token.is_punct]
print(list(sp.vocab.strings))
#print(set(sp.vocab.strings))
