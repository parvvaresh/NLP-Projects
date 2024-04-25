import pandas as pd
import numpy as np

class freqword:
  def __init__(self, data, words_col, target_col):
    self.data = data
    self.words_col = words_col
    self.target_col = target_col
    self.targets = data[self.target_col].unique()
    self.words = self.get_words(self.data[self.words_col])

    self.counter = self.create_counter()

  def transform(self):
    val = []
    for index in range(0 , self.data.shape[0]):
      words = self.data.iloc[index][self.words_col]
      target = self.data.iloc[index][self.target_col]
      for word in words:
        count_target = self.counter[word].copy()
        count_target[target] += 1
        self.counter[word] = count_target

    for key in self.counter:
        count_target = self.counter[key].copy()
        count = list(count_target.values())
        self.counter[key] = np.array(count)


    for index in range(0 , self.data.shape[0]):
      words = self.data.iloc[index][self.words_col]
      x = 0
      for word in words:
        count_target = self.counter[word].copy()
        x += count_target
      val.append(x)
    return np.array(val)

  def create_counter(self):
    count_targets = dict()
    for target in self.targets:
      count_targets[target] = 0

    counter = dict()
    for word in self.words:
      temp = count_targets.copy()
      counter[word] = temp
    return counter

  def get_words(self, all_words):
    words = []
    for element in all_words:
      words.extend(element)
    return list(set(words))