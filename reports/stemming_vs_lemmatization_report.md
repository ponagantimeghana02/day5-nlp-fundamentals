# Stemming and Lemmatization Report

## Introduction

Stemming and Lemmatization are text preprocessing techniques used in Natural Language Processing (NLP). Both methods reduce words to their base form, helping machine learning models process text more efficiently.

## Stemming

Stemming removes prefixes or suffixes from words using simple rule-based techniques. It does not consider the context or meaning of the word.

Examples:

* running → run
* playing → play
* studies → studi

Advantages:

* Fast and computationally efficient.
* Useful for search engines and information retrieval systems.

Disadvantages:

* May produce non-dictionary words.
* Ignores grammatical meaning.

## Lemmatization

Lemmatization reduces a word to its dictionary form (lemma) using vocabulary and linguistic analysis. It considers the word's meaning and part of speech.

Examples:

* running → run (when treated as a verb)
* studies → study
* cars → car
* better → good (when treated as an adjective)

Advantages:

* Produces meaningful dictionary words.
* More accurate than stemming.

Disadvantages:

* Slower than stemming.
* Requires additional linguistic resources.

## Comparison

| Original Word | Stemmed Form | Lemmatized Form |
| ------------- | ------------ | --------------- |
| running       | run          | run             |
| playing       | play         | play            |
| studies       | studi        | study           |
| better        | better       | good            |
| cars          | car          | car             |

## Conclusion

Stemming is faster but less accurate because it simply trims word endings. Lemmatization is slower but more accurate because it uses linguistic knowledge to find the actual root word. For modern NLP applications, lemmatization is generally preferred when accuracy is important.
