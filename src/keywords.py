from sklearn.feature_extraction.text import CountVectorizer

def get_keywords(text, top_n=3):
    vectorizer = CountVectorizer(
        stop_words="english",
        ngram_range=(1, 1),
    )

    matrix = vectorizer.fit_transform([text])
    words = vectorizer.get_feature_names_out()
    counts = matrix.toarray()[0]

    ranked = sorted(
        zip(words, counts),
        key=lambda item: item[1],
        reverse=True,
    )

    return [word for word, _ in ranked[:top_n]]

if __name__ == "__main__":
    sample = (
        "Machine learning allows computers to learn patterns from data "
        "and use those patterns to make predictions."
    )

    print(get_keywords(sample))
