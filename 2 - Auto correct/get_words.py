from model.edit_distance  import edit_distance
from model.jaccard_similarity import jaccard_similarity
import pandas as pd

class get_words:
	def __init__(self):
		self.words_en = pd.read_csv("words_en.csv")["words"].dropna()
		self.words_en = self.words_en.to_list()
		self.words_fa = pd.read_csv("words_fa.csv")["words"].dropna()
		self.words_fa = self.words_fa.to_list()
		self.edit_distance = edit_distance()
		self.jaccard_similarity = jaccard_similarity()



	def get(self, writer, lan):
		if lan == "en":
			if writer in self.words_en:
				print("this is word is correct but Maybe this is not what you mean and we will display similar words that you might mean")

			result_ed = dict()
			result_js = dict()
			print("				please wait")

			for word in self.words_en:
				if isinstance(len(word), type(float)):
					continue
				else:	
					result_ed.update({word : self.edit_distance.get_score(writer, word)})
					result_js.update({word : self.jaccard_similarity.get_score(writer, word)})


			result_ed = dict(sorted(result_ed.items(), key = lambda item : item[1]))
			result_js = dict(sorted(result_js.items(), key = lambda item : item[1]))


			return {

				"edit distance" : dict(list(result_ed.items())[ : 5]),
				"jaccard similarity" : dict(reversed(list(dict(list(result_js.items())[-5 : ]).items())))
	,

			}

		if lan == "fa":
			if writer in self.words_fa:
				print("this is word is correct but Maybe this is not what you mean and we will display similar words that you might mean")


			result_ed = dict()
			result_js = dict()
			print("				please wait")

			for word in self.words_fa:
				if isinstance(len(word), type(float)):
					continue
				else:	
					result_ed.update({word : self.edit_distance.get_score(writer, word)})
					result_js.update({word : self.jaccard_similarity.get_score(writer, word)})

			if writer in result_ed:
				result_ed.pop(writer)

			if writer in result_js:
				result_js.pop(writer)

			result_ed = dict(sorted(result_ed.items(), key = lambda item : item[1]))
			result_js = dict(sorted(result_js.items(), key = lambda item : item[1]))


			return {

				"edit distance" : dict(list(result_ed.items())[ : 5]),
				"jaccard similarity" : dict(reversed(list(dict(list(result_js.items())[-5 : ]).items())))
	,

			}

