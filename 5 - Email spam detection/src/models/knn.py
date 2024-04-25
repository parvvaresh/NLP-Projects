import numpy as np

class knn:
  def __init__(self):
    self.k = None
  
  def fit(self, X_train, y_train):
    self.X_train = X_train
    self.y_train = y_train
  
  def predict(self, x_test, k):
    self.k = k
    y_pred = [self._predict(x, k) for x in x_test]
    return np.array(y_pred)
  
  def _predict(self, x, k):
    euclidean_distance = [self._euclidean_distance(x_train, x) for x_train in self.X_train]
    index_sort = np.argsort(euclidean_distance)[ : self.k]
    labels = [self.y_train[index] for index in index_sort]
    return self.get_most_label(labels)
  
  def get_most_label(self, labels):
    counter = {}
    for label in labels:
      if label in counter:
        counter[label] += 1
      else:
        counter[label] = 1
    return max(counter.items() , key=lambda item : item[1])[0]

  def _euclidean_distance(self, x_1, x_2):
    return np.sqrt(np.sum((x_1 - x_2) ** 2))
  
  def accuracy(self, y, y_predict):
    return np.sum(y == y_predict) / len(y)
