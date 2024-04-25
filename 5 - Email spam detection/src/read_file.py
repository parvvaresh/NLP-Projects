import pandas as pd
import os
from data.get_path import get_ham, get_spam

def _create_dataset(paths, label):
  data = list()
  for path in paths:
    with open(path, encoding='utf-8') as f:
      temp = f.read()
      data.append(temp)

  df = pd.DataFrame()
  df["Text"] = data
  df["label"] = label
  return df

def create_dataset():

  spam = _create_dataset(get_spam(), "spam")
  ham = _create_dataset(get_ham(), "ham")


  df = pd.concat([spam, ham ], axis=0)
  df["target"] = df["label"].replace(["spam", "ham"], [1, 0])

  return df
