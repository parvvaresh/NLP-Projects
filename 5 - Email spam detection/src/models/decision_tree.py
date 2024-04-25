import numpy as np

class Node:
  def __init__(self, feature = None, threshold = None, left = None, right = None, value = None):
    self.feature = feature
    self.threshold = threshold
    self.left = left
    self.right = right
    self.value = value

  def is_leaf(self):
    return self.value is not None

class decision_tree:
  def __init__(self, min_samples_split = 2, max_depth = 100, n_feats = None):
    self.min_samples_split = min_samples_split
    self.max_depth = max_depth
    self.n_feats = n_feats

    self.root = None

  def fit(self, x, y):
    self.n_feats = x.shape[1] if not self.n_feats else min(x.shape[1] , self.n_feats)
    self.root = self._grow_tree(x, y)

  def _grow_tree(self, x, y, depth = 0):
    n_samples , n_feature = x.shape
    n_labels = len(np.unique(y))

    if (depth >= self.max_depth) or (n_labels == 1) or (n_samples < self.min_samples_split):
      leaf_value = self._most_common_label(y)
      return Node(value = leaf_value)

    features_index = np.random.choice(n_feature, self.n_feats, replace=False)
    best_feature, best_threshold = self._best_split(x, y, features_index)
    left_index , right_index = self._split(x[ : , best_feature], best_threshold)

    left_child = self._grow_tree(x[left_index, : ], y[left_index] , depth + 1)
    right_child = self._grow_tree(x[right_index, : ], y[right_index] , depth + 1)
    return Node(best_feature, best_threshold, left_child, right_child)



  def _best_split(self, x, y, features_index):
    best_gain = -1
    best_feature_index , best_threshold = None, None

    for feature_index in features_index:
      x_column = x[ : , feature_index]
      thresholds = np.unique(x_column)
      for threshold in thresholds:
        gain = self._information_gain(y, x_column, threshold)
        if gain > best_gain:
          best_gain = gain
          best_feature_index = feature_index
          best_threshold = threshold

    return best_feature_index, best_threshold

  def _information_gain(self, y,  x_column, threshold):
    entropy_parents = self._entropy(y)

    left_index, right_index = self._split(x_column, threshold)

    if len(left_index) == 0 or len(right_index) == 0:
      return 0

    n_all , n_left , n_right = len(y),  len(left_index) ,  len(right_index)
    entropy_left , entropy_right = self._entropy(y[left_index]) , self._entropy(y[right_index])

    entropy_childerns = ((n_left / n_all) * entropy_left) + ((n_right / n_all) * entropy_right)
    information_gain = entropy_parents - entropy_childerns
    return information_gain

  def _split(self, x, threshold):
    left_index = np.argwhere(x <= threshold).flatten()
    right_index = np.argwhere(x > threshold).flatten()
    return left_index, right_index

  def _entropy(self, y):
    counter = dict()
    for label in y:
      if label in counter:
        counter[label] += 1
      else:
        counter[label] = 1

    ps = np.array(list(counter.values())) / len(y)
    return -np.sum([p * np.log2(p) for p in ps if p > 0])

  def _most_common_label(self, y):
    counter = dict()
    for label in y:
      if label in counter:
        counter[label] += 1
      else:
        counter[label] = 1
    counter = dict(sorted(counter.items() , key=lambda  item : item[1]))
    most_common = list(counter.keys())[-1]
    return most_common

  def predict(self, x):
    return np.array([self._traverse_tree(point, self.root) for point in x])

  def _traverse_tree(self, x, node):
    if node.is_leaf():
      return node.value

    if x[node.feature] <= node.threshold:
      return self._traverse_tree(x, node.left)
    return self._traverse_tree(x, node.right)

  def accuracy(self, y_test, y_pred):
     accu = np.sum(y_test == y_pred) / len(y_test)
     return accu
