import string
import re








class pre_process:
	def __init__(self):
		self.punctuation_en = string.punctuation
		persian_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
		self.punctuations_list = string.punctuation + persian_punctuations


	def process(self, text, lan = "en"):
		if lan == "en":
			return self._preprocess_engilish(text)
		elif lan == "fa":
			return self._preprocess_farsi(text)


	def _preprocess_farsi(self, text):
		text = self._remove_punctuations(text)
		return text

	def _preprocess_engilish(self, text):
		text = text.lower()
		text = text.lstrip()
		text = text.rstrip()
		text = "".join([char for char in text if char not in self.punctuation_en])
		return text


	def _remove_punctuations(self, text):
	    translator = str.maketrans('', '', self.punctuations_list)
	    return text.translate(translator)

