import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Artificial Intelligence is transforming software development rapidly."

word_tokens = word_tokenize(text)

sentence_tokens = sent_tokenize(text)

print("Word Tokens:")
print(word_tokens)

print("\nSentence Tokens:")
print(sentence_tokens)