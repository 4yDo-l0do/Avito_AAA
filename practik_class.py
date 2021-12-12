from math import log


def tf_transform(count_matrix):
    """считает частоту встречаемости каждого слова в массиве слов"""

    result = []

    for vector in count_matrix:
        word_count = sum(vector)
        tf_transform_row = [round(i / word_count, 3) for i in vector]
        result.append(tf_transform_row)

    return result


def idf_transform(count_matrix):
    """считает логарифм частоты встречаемости каждого слова в каждом документе"""

    result = []
    n_doc = len(count_matrix)
    for word in range(len(count_matrix[0])):
        n_doc_with_word = 0
        for vector in count_matrix:
            if vector[word] > 0:
                n_doc_with_word += 1
        result.append(round(log((n_doc + 1) / (n_doc_with_word + 1)) + 1, 1))
    return result


class TfidfTransformer:
    """tf_transform*idf_transform"""

    def fit_transform(self, count_matrix):
        tf = tf_transform(count_matrix)
        idf = idf_transform(count_matrix)

        tf_idf = []
        for value in tf:
            tf_idf.append([round(a * b, 3) for a, b in zip(value, idf)])

        return tf_idf


class CountVectorizer:
    """Convert a collection of text documents to a matrix of token counts"""

    def __init__(self):
        self.__feature_names = []

    def fit_transform(self, corpus):
        """создает словарь с уникальными значениями и формерует по нему терм-документную матрицу"""
        result = []
        # создаем список с уникальными словами
        for line in corpus:
            for word in line.split():
                if word.lower() not in self.__feature_names:
                    self.__feature_names.append(word.lower())
        # находим сколько раз встречается слово
        for line in corpus:
            dict_names = dict.fromkeys(self.__feature_names, 0)
            for word in line.split():
                dict_names[word.lower()] += 1
            result.append([count for count in dict_names.values()])
        return result

    def get_feature_names(self):
        """возвращает список уникальных слов"""
        return self.__feature_names


class TfidfVectorizer(CountVectorizer):
    """класс TfidfVectorizer, имеющий метод fit_transform"""

    def __init__(self):
        super().__init__()
        self._tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
