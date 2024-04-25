from math import log
import numpy as np
import pandas as pd

class tfidf:
  def __init__(self):
    pass

  def fit(self, df, col):
    self.ducs = list(df[col])
    self.size_duc = len(self.ducs)
    self.all_words = self.collet_words(self.ducs)
    self.word_index = self.create_word_index(self.all_words)
    self.word_count = self.create_word_count(self.ducs)
    return self.tf_idf()

  def _tf_idf(self, duc):
    vec = np.zeros((len(self.all_words),))
    for word in duc:
        tf = self.tf(duc, word)
        idf = self.idf(word)
        vec[self.word_index[word]] = tf * idf
    return vec

  def create_word_index(self, all_words):
    word_index = {}
    for i, word in enumerate(all_words):
      word_index[word] = i
    return word_index

  def tf_idf(self):
    vectors = []
    for duc in self.ducs:
      vectors.append(self._tf_idf(duc))
    return np.array(vectors)

  def tf(self, document, word):
      N = len(document)
      occurance = len([token for token in document if token == word])
      return occurance / N

  def idf(self, word):
      try:
          word_occurance = self.word_count[word] + 1
      except:
          word_occurance = 1
      return np.log(self.size_duc / word_occurance)

  def collet_words(self, ducs):
    words = []
    for element in ducs:
      words.extend(element)
    return list(set(words))

  def create_word_count(self , ducs):
    words = []
    for element in ducs:
      words.extend(element)
    word_count = {}
    for word in words:
      if word in word_count:
        word_count[word] += 1
      else:
        word_count[word] = 1
    return word_count