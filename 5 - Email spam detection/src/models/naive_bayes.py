import numpy as np

class naive_bayes:
  def __init__(self):
    pass

  def fit(self, x, y):
    self.m, self.n = x.shape
    self._classes = np.unique(y)
    self._mean = np.zeros((self._classes.shape[0], self.n))
    self._var = np.zeros((self._classes.shape[0], self.n))
    self._y_possibilities = np.zeros(self._classes.shape[0])

    for index , Class in enumerate(self._classes):
      class_temp = x[y == Class]
      self._mean[index, : ] = np.mean(class_temp, axis = 0)
      self._var[index, : ] = np.var(class_temp, axis = 0)
      self._y_possibilities[index] = class_temp.shape[0] / self.m


  def predict(self, X):
    y_predict = [self._predict(x) for x in X]
    return np.array(y_predict)

  def _predict(self, point):
    result = []
    for index in range(self._classes.shape[0]):
      y_possibility = self._y_possibilities[index]
      p_x_y = self._p_x_y(point, index)
      possibility = y_possibility * p_x_y
      result.append(possibility)
    index_max = result.index(max(result))
    return self._classes[index_max]

  def _p_x_y(self, point, index):
    mean = self._mean[index]
    var = self._var[index]
    denominator = np.sqrt(2 * np.pi * var)
    numerator = np.exp(-((point - mean) ** 2) / (2 * var))

    result = 1
    for p in (numerator / denominator):
      result *= p
    return result

  def accuracy(self, y, y_predict):
    return np.sum(y == y_predict) / y.shape[0]
