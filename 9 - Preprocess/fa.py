"""
    in the name of god
        this is strong pre-process persian text 
"""
import hazm
import re
import string
import matplotlib.pyplot as plt

import dadmatools.pipeline.language as language





class PreProcess:
    def __init__(self):
        """
            Initialization of functions and objects used during work
        """
        persian_punctuations = '''`÷×؛#<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
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
        self.spell_checker =  language.Pipeline('spellchecker')
        self.informal2formal = language.Pipeline('itf')




    def remove_punctuations(self, text):
        """
            The remove_punctuations function takes a string (text) as input and removes punctuation marks (such as periods, commas, question marks, etc.) from it.
        """
        translator = str.maketrans('', '', self.punctuations_list)
        return text.translate(translator)
    
    
    def remove_diacritics(self, text):
        """
            The remove_diacritics function is used to remove diacritics from a text.
        """
        text = re.sub(self.arabic_diacritics, '', text)
        return text
    
    
    def normalize_persian(self, text):
        """
            The normalize_persian function normalizes the text given to it using these changes and finally returns a text with standard Persian characters and no extra spaces.
        """
        text = re.sub("[إأآا]", "ا", text)
        text = re.sub("ي", "ی", text)
        text = re.sub("ؤ", "و", text)
        text = re.sub("ئ", "ی", text)
        text = re.sub("ة", "ه", text)
        text = re.sub("ك" ,"ک" , text)
        text = re.sub("[^ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]", " ", text)
        text = re.sub("[^\S\n\t]+", ' ', text)
        return text
    
    
    def handle_special_characters(self, text):
        text = re.sub(r'[^\w\s]', '', text)
        return text
    
    def remove_repeating_char(self, text):
        return re.sub(r'(.)\1+', r'\1', text)
    
    
    def informal2formal(self, text):
        return str(self.informal2formal(text)["itf"])
    
    
    
    def spell_check(self, text):
        return str(self.spell_checker(text)["spellchecker"]["corrected"])
    
    
    def tokenize(self, text):
        return hazm.word_tokenize(text)
    
    def remove_stopwords(self, tokens):
        return [token for token in tokens if token not in self.stop_words]
    
    
    def lemmatizer_text(self, tokens):
        return [self.lemmatizer.lemmatize(token) for token in tokens]