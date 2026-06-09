import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

with open("chat_messages.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()

text = re.sub(r'https?://\S+', '', text)

text = re.sub(r'\S+@\S+', '', text)

text = re.sub(r'[^a-zA-Z\s]', '', text)

text = re.sub(r'\s+', ' ', text).strip()


tokens = text.split()


stop_words = set(stopwords.words('english'))

filtered_tokens = [
    word for word in tokens
    if word not in stop_words
]


lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word)
    for word in filtered_tokens
]


keyword_frequency = Counter(lemmatized_words)

top_keywords = keyword_frequency.most_common(20)



with open("chat_report.txt", "w", encoding="utf-8") as report:

    report.write("AI CHAT PREPROCESSING REPORT\n")
    report.write("=" * 50 + "\n\n")

    report.write("CLEANED TEXT\n")
    report.write("-" * 50 + "\n")
    report.write(text + "\n\n")

    report.write("TOKENS\n")
    report.write("-" * 50 + "\n")
    report.write(str(tokens) + "\n\n")

    report.write("AFTER STOP WORD REMOVAL\n")
    report.write("-" * 50 + "\n")
    report.write(str(filtered_tokens) + "\n\n")

    report.write("LEMMATIZED WORDS\n")
    report.write("-" * 50 + "\n")
    report.write(str(lemmatized_words) + "\n\n")

    report.write("TOP KEYWORDS\n")
    report.write("-" * 50 + "\n")

    for keyword, count in top_keywords:
        report.write(f"{keyword:<20} {count}\n")

print("Report generated successfully!")
print("Saved as chat_report.txt")