from textblob import TextBlob

reviews = [
    "This course is amazing",
    "The training is excellent",
    "The project is difficult",
    "The application is terrible"
]

print("Sentiment Analysis Results")
print("-" * 60)

positive = 0
negative = 0
neutral = 0

for review in reviews:
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
        positive += 1
    elif polarity < 0:
        sentiment = "Negative"
        negative += 1
    else:
        sentiment = "Neutral"
        neutral += 1

    print(f"Review: {review}")
    print(f"Polarity: {polarity}")
    print(f"Sentiment: {sentiment}")
    print("-" * 60)

print("\nSentiment Summary")
print(f"Positive Reviews: {positive}")
print(f"Negative Reviews: {negative}")
print(f"Neutral Reviews: {neutral}")