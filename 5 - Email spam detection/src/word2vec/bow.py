import numpy as np

class bow:
    def __init__(self):
        pass

    def fit(self, df, col):
        temp = df[col]
        ducs = list(temp)
        self.mapping = self._collect_index_unique_words(ducs)
        self.inverse_mapping = {index : word for word , index in self.mapping.items()}
        self.counter_words = self._counter(ducs)


    def transform(self, df, col):

        temp = df[col]
        ducs = list(temp)
        if not self.mapping:
            raise ValueError("BOW has not been fitted. Call fit() first.")

        vectors = []
        number_of_unique_words = len(self.mapping)
        for duc in ducs:
            words = duc
            vector = [0] * number_of_unique_words
            for word in words:
                vector[self.mapping[word]] = self.counter_words[word]
            vectors.append(vector)

        return np.array(vectors)



    def inverse_transform(self, vectors):
        ducs = []
        for vector in vectors:
            vector = list(vector)
            duc = []
            for index, vec in enumerate(vector):
                if vec != 0:
                    duc.append(self.inverse_mapping[index])
            ducs.append(duc)
        return ducs


    def _collect_index_unique_words(self, ducs):
        unique_words = []
        for duc in ducs:
            words = duc
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)



        index_unique_words = {}
        for index , word in enumerate(unique_words):
            index_unique_words[word] = index
        return index_unique_words



    def _counter(self,  ducs):
        counter = {}
        for duc in ducs:
            words = duc
            for word in words:
               if word not in counter:
                   counter[word] = 1
               elif word in counter:
                   counter[word] += 1

        return counter
