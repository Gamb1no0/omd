from TfidfVectorizer import TfidfVectorizer


def main():
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    for tfidf_vector in tfidf_matrix:
        print([el for el in tfidf_vector])


if __name__ == '__main__':
    main()