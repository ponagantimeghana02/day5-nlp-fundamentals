import re
import nltk

for resource in ['punkt', 'punkt_tab']:
    try:
        nltk.data.find(f'tokenizers/{resource}')
    except LookupError:
        nltk.download(resource)

from nltk.tokenize import word_tokenize

text = """
Hello Everyone!!!

Welcome to AI/ML Training.

Contact us at support@company.com

Visit https://company.com

Call 9876543210
"""

text = text.lower()
text = re.sub(r'https?://\S+', '', text)
text = re.sub(r'\S+@\S+', '', text)
text = re.sub(r'\b\d{10}\b', '', text)
text = re.sub(r'[^a-zA-Z\s]', '', text)

tokens = word_tokenize(text)

print("Tokens:")
print(tokens)

print("\nCleaned Text:")
print(" ".join(tokens))