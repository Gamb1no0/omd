from typing import List


class CountVectorizer:
    '''Ковертирует коллекцию текстов в терм-документную матрицу'''

    def __init__(self) -> None:
        self.__feature_names = None

    def make_feature_names(self, corpus: List[str]) -> List[str]:
        '''Создает вектор для атрибута __feature_names.

        Метод получает блок текстов corpus и собирает их в вектор
        уникальных слов, приведенныхз в нижний регистр.'''

        set_words = set()
        feature_names = []

        if not isinstance(corpus, list):
            raise TypeError('List corpus expected.')
        for text in corpus:
            if not isinstance(text, str):
                raise TypeError(f'String object expected but get {type(text)}')
            for word in map(lambda x: x.lower(), text.split()):
                if word not in set_words:
                    set_words.add(word)
                    feature_names.append(word)
        return feature_names

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        '''Возвращает терм-документную матрицу

        Получает на вход коллекцию текстов и конвертирут коллекцию
        в набор вектор с подсчитанным колличеством вхождением
        каждого слова.
        '''

        self.__feature_names = self.make_feature_names(corpus)
        count_matrix = [[0 for _ in range(len(self.__feature_names))]
                        for _ in range(len(corpus))]
        for index_text in range(len(corpus)):
            for word in corpus[index_text].lower().split():
                index_word = self.__feature_names.index(word)
                count_matrix[index_text][index_word] += 1
        return count_matrix

    def get_feature_names(self) -> List[str]:
        '''Возвращает значение атрибута класса'''

        return self.__feature_names
