import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

with open("resume.txt", "r", encoding="utf-8") as file:
    text = file.read()


text = text.lower()

text = re.sub(r'https?://\S+', '', text)

text = re.sub(r'\S+@\S+', '', text)

text = re.sub(r'\b\d{10}\b', '', text)

text = re.sub(r'[^a-zA-Z\s]', '', text)

text = re.sub(r'\s+', ' ', text).strip()



tokens = text.split()



stop_words = set(stopwords.words('english'))

filtered_tokens = [
    word for word in tokens
    if word not in stop_words
]


keyword_freq = Counter(filtered_tokens)

top_keywords = keyword_freq.most_common(20)


with open("keyword_report.txt", "w", encoding="utf-8") as report:

    report.write("RESUME KEYWORD ANALYSIS REPORT\n")
    report.write("=" * 40 + "\n\n")

    report.write("Top 20 Keywords\n")
    report.write("-" * 40 + "\n")

    for keyword, count in top_keywords:
        report.write(f"{keyword:<20} {count}\n")

print("Keyword report generated successfully!")
print("Saved as keyword_report.txt")