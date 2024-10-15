import string
import re
import hazm



class PreProcess:
    def __init__(self) -> None:
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
    
    def remove_punctuations(self, text : str) -> str:
        translator = str.maketrans('', '', self.punctuations_list)
        return text.translate(translator)
    
    def remove_diacritics(self, text : str) -> str:
        text = re.sub(self.arabic_diacritics, '', text)
        return text 
    
    def normalize_persian(self, text : str) -> str:
        text = re.sub("[إأآا]", "ا", text)
        text = re.sub("ي", "ی", text)
        text = re.sub("ؤ", "و", text)
        text = re.sub("ئ", "ی", text)
        text = re.sub("ة", "ه", text)
        text = re.sub("ك" ,"ک" , text)
        text = re.sub("[^ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]", " ", text)
        text = re.sub("[^\S\n\t]+", ' ', text)
        return text
    
    def remove_repeating_char(self, text : str) -> str:
        return re.sub(r'(.)\1+', r'\1', text)
    
    def tokenize(self, text : str) -> list:
        return hazm.word_tokenize(text)
    
    def remove_stopwords(self, tokens : list) -> list:
        return [token for token in tokens if token not in self.stop_words]
    
    def lemmatizer_text(self, tokens : list) -> list:
        return [self.lemmatizer.lemmatize(token) for token in tokens]
    
    
    def pipline(self, text : str) -> list:
        text = self.remove_punctuations(text)
        text = self.remove_diacritics(text)
        text = self.normalize_persian(text)
        text = self.remove_repeating_char(text)
        tokens = self.tokenize(text)
        tokens = self.remove_stopwords(tokens)
        tokens = self.lemmatizer_text(tokens)
        return tokens