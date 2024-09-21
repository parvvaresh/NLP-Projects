"""
    in the name of god
        this is strong pre-process engilsh text 
"""

import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from autocorrect import Speller
import re
import contractions
from word2number import w2n
import unicodedata

class PreProcess:
    def __init__(self):
        """
            Initialization of functions and objects used during work
        """
        self.spell = Speller(lang='en')
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))


    def remove_special_characters(self, text : str) -> str : 
        """
            Here, special characters are removed from the text
            In the first step , links and site addresses are removed from the text
            In the second step, all non-English characters are removed from the text, which can be referred to as emojis.
            In the third step, all punctuation marks are removed from the text
            In the fourth step, special characters are removed, such as @
            In the fifth step, all characters except English letters, numbers and spaces are removed
        """
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = text.encode('ascii', 'ignore').decode('ascii')
        text = ''.join([char for char in text if char not in string.punctuation])
        text = re.sub(r'[@#$%^&*()_+]', '', text)
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text
    


    def spell_check(self, text : str) -> str:
        """
            This function is used to correct the spelling of text (words).
        """
        return self.spell(text)    

    def tokenize_text(self, text : str) -> list:
        """
            Convert a sentence into tokens
        """
        tokens = word_tokenize(text)
        return tokens
    


    def _case_normalization(self, tokens : list) -> list:
        """
            Normalize words by converting them to lowercase letters
        """
        return [token.lower() for token in tokens]

    def _remove_accents_diacritics(self, tokens : list) -> list:
        """
            A list of tokens (words) is used to remove letters with a specific combination (such as letters with Arabic or mixed symbols). 
            Specifically, it uses the unicodedata.normalize function with the NFD form, 
            which isolates mixed characters (such as Arabic) and then removes all characters that are in the Mn category (combined characters such as Arabic).
                ex : café -- > cafe
        """
        return [''.join(c for c in unicodedata.normalize('NFD', token) if unicodedata.category(c) != 'Mn') for token in tokens]

    def _expand_contractions(self, tokens):
        """
            The expand_contractions function is designed to expand contractions in a list of tokens (words). 
            Abbreviations are shortened forms of words or phrases that are usually written with an apostrophe (in addition to "don't" in "do not").
        """
        return [contractions.fix(token) for token in tokens]


    def _normalize_numbers_and_units(self, tokens):
        """
            Units of measurement and numbers are used in a list of tokens. 
            This will convert all units of measurement and numbers into a standard format.
        """
        normalized_tokens = []
        for token in tokens:
            token = re.sub(r'\bkm\b', 'kilometres', token)  # km -> kilometres
            token = re.sub(r'\bapprox\.\b', 'approximately', token)  # approx. -> approximately
            token = re.sub(r'\bcm\b', 'centimetres', token)  # cm -> centimetres
            token = re.sub(r'\bkg\b', 'kilograms', token)  # kg -> kilograms
            token = re.sub(r'\blbs\b', 'pounds', token)  # lbs -> pounds
            token = re.sub(r'\bmm\b', 'millimetres', token)  # mm -> millimetres
            token = re.sub(r'\bml\b', 'millilitres', token)  # ml -> millilitres
            token = re.sub(r'\bl\b', 'litres', token)  # l -> litres
            token = re.sub(r'\bsec\b', 'seconds', token)  # sec -> seconds
            token = re.sub(r'\bmin\b', 'minutes', token)  # min -> minutes
            token = re.sub(r'\bhr\b', 'hours', token)  # hr -> hours
            token = re.sub(r'\bhrs\b', 'hours', token)  # hrs -> hours
            token = re.sub(r'\bft\b', 'feet', token)  # ft -> feet
            token = re.sub(r'\bin\b', 'inches', token)  # in -> inches
            token = re.sub(r'\bmph\b', 'miles per hour', token)  # mph -> miles per hour
            token = re.sub(r'\bkph\b', 'kilometres per hour', token)  # kph -> kilometres per hour
            token = re.sub(r'\bm\s\b', 'metres per second', token)  # m/s -> metres per second
            token = re.sub(r'\bsec\b', 'seconds', token)  # sec -> seconds

            try:
                token = str(w2n.word_to_num(token)) if token.isdigit() else token
            except ValueError:
                pass

            normalized_tokens.append(token)
        return normalized_tokens


    def normalize_text(self, tokens):
        """
            The sequence of activities to convert a text into normal text:
                1- shorten words
                2- Removal of Arabs
                3- Converting abbreviations to normal
                4- will convert all units of measurement and numbers into a standard format
        """
        tokens = self._case_normalization(tokens)
        tokens = self._remove_accents_diacritics(tokens)
        tokens = self._expand_contractions(tokens)
        tokens = self._normalize_numbers_and_units(tokens)
        return tokens


    


    def remove_stopwords(self,tokens):
        """
            This line of code is used to remove stop words from a list of tokens (words). 
            Stop words are usually words that are very common in natural language and, in most cases, 
            are not important for text analysis (such as "the", "is", "and" in English).
        """
        return [token for token in tokens if token not in self.stop_words]
    


    def lemmatization(self, tokens : list) -> list:
        """
            This code function uses Lemmatization to convert each token to its base or root form. 
            Lemmatization is a process in natural language processing (NLP) that aims to convert words into their basic or root form, 
            taking into account the word's role in the sentence (such as noun, verb, adjective). 
            This helps to convert synonyms to a standard root or form.
            then remove stopwords
        """
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens] 
        tokens = self.remove_stopwords(tokens)
        return tokens