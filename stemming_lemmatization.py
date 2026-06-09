import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

words = [
    "running",
    "playing",
    "studies",
    "better",
    "cars"
]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Word\t\tStemmed\t\tLemmatized")
print("-" * 40)

for word in words:
    stemmed = stemmer.stem(word)
    lemmatized = lemmatizer.lemmatize(word)
    
    print(f"{word}\t\t{stemmed}\t\t{lemmatized}")