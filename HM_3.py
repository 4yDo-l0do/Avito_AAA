class CountVectorizer:
    """Convert a collection of text documents to a matrix of token counts."""
    def __init__(self):
        self.__feature_names = []

    def fit_transform(self, corpus):
        """создает словарь с уникальными значениями и формерует по нему терм-документную матрицу"""
        result = []
        #создаем список с уникальными словами
        for line in corpus:
            for word in line.split():
                if word.lower() not in self.__feature_names:
                    self.__feature_names.append(word.lower())
        #находим сколько раз встречается слово
        for line in corpus:
            dict_names = dict.fromkeys(self.__feature_names, 0)
            for word in line.split():
                dict_names[word.lower()] += 1
            result.append([count for count in dict_names.values()])
        return result


    def get_feature_names(self):
        """возвращает список уникальных слов"""
        return self.__feature_names

if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
