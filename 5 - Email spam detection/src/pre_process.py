import hazm 
import string
import re
import pandas as pd


class preprocessing:
  def __init__(self):
    persian_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
    self.punctuations_list = string.punctuation + persian_punctuations
    self.arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    self.stop_words = hazm.stopwords_list()
    self.lemmatizer = hazm.Lemmatizer()

  def fit(self, train_data):
    train_data['Text'] = train_data['Text'].apply(self._remove_diacritics)
    train_data['Text'] = train_data['Text'].apply(self._remove_punctuations)
    train_data['Text'] = train_data['Text'].apply(self._remove_repeating_char)
    train_data['Text'] = train_data['Text'].apply(self._normalize_persian)
    train_data['Text'] = train_data['Text'].apply(self._tokenize)
    train_data['Text'] = train_data['Text'].apply(self._remove_stopwords)
    train_data['Text'] = train_data['Text'].apply(self._lemmatizer)
    return train_data


  def _remove_diacritics(self, text):
    text = re.sub(self.arabic_diacritics, '', text)
    return text

  def _remove_punctuations(self, text):
    translator = str.maketrans('', '', self.punctuations_list)
    return text.translate(translator)

  def _remove_repeating_char(self, text):
    return re.sub(r'(.)\1+', r'\1', text)


  def _normalize_persian(self, text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ي", "ی", text)
    text = re.sub("ؤ", "و", text)
    text = re.sub("ئ", "ی", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("ك" ,"ک" , text)
    text = re.sub("[^ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]", " ", text)
    text = re.sub("[^\S\n\t]+", ' ', text)
    return text


  def _tokenize(self, text):
    return text.split()

  def _remove_stopwords(self, words):
    return [word  for word in words if word not in self.stop_words]

  def _lemmatizer(self, words):
    result = set()
    for token in words:
      result.add(self.lemmatizer.lemmatize(token))
    return list(result)
