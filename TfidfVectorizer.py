from CountVectorizer import CountVectorizer
from TfidfTransformer import TfidfTransformer


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tf_idf_transformer = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        """Вычисляет TF-IDF матрицу для списка текстов"""
        corpus_matrix = super().fit_transform(corpus)

        return self.tf_idf_transformer.fit_transform(corpus_matrix)
