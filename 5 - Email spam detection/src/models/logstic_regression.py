import numpy as np

class logstic_regression:
  def __init__(self, max_iter = 100000, learning_rate = 1e-6):
    self.max_iter = max_iter
    self.learning_rate = learning_rate
    self.costs = []

  def fit(self, X, y):
    self.m, self.n = X.shape
    y = y.reshape(self.m ,1)
    self.weights = np.zeros((self.n , 1))
    self.baias = 0
    for _ in range(0, self.max_iter):
      y_predict = self.sigmoid(np.dot(X, self.weights) + self.baias)

      loss = - np.dot(y.T, np.log(y_predict)) - np.dot((1 - y).T, np.log(1 - y_predict))
      cost = np.sum(loss) / self.m
      self.costs.append(cost)

      dw = np.dot(X.T, y_predict -  y) / self.m
      db = np.sum(y_predict -  y) / self.m

      self.weights -= self.learning_rate * dw
      self.baias -= self.learning_rate * db

  def predict(self, x):
    y_temp = self.sigmoid(np.dot(x, self.weights) + self.baias)
    y_pred = [1 if element >= 0.5 else 0 for element in y_temp]
    return np.array(y_pred)

  def sigmoid(self, x):
    return 1 / (1 + np.exp(-x))

  def accuracy(self, y, y_pred):
    return np.sum(y == y_pred) / len(y)

  def show_costs(self):
    import matplotlib.pyplot as plt
    plt.plot(self.costs)
