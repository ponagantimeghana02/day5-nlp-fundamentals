import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

text = "Artificial Intelligence is one of the most important technologies in the world."

words = word_tokenize(text)

stop_words = set(stopwords.words('english'))

filtered_words = [word for word in words if word.lower() not in stop_words]

processed_text = " ".join(filtered_words)

print("Original Text:")
print(text)

print("\nProcessed Text:")
print(processed_text)