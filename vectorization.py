from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Dataset
documents = [
    "AI is transforming businesses",
    "Machine learning powers AI",
    "Deep learning is a subset of AI",
    "AI applications are growing rapidly"
]

# -------------------------
# Bag of Words
# -------------------------
bow_vectorizer = CountVectorizer()

bow_matrix = bow_vectorizer.fit_transform(documents)

print("=== Bag of Words ===")
print("Vocabulary:")
print(bow_vectorizer.vocabulary_)

print("\nFeature Names:")
print(bow_vectorizer.get_feature_names_out())

print("\nMatrix Shape:")
print(bow_matrix.shape)

print("\nBoW Matrix:")
print(bow_matrix.toarray())


# -------------------------
# TF-IDF
# -------------------------
tfidf_vectorizer = TfidfVectorizer()

tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

print("\n\n=== TF-IDF ===")
print("Vocabulary:")
print(tfidf_vectorizer.vocabulary_)

print("\nFeature Names:")
print(tfidf_vectorizer.get_feature_names_out())

print("\nMatrix Shape:")
print(tfidf_matrix.shape)

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())