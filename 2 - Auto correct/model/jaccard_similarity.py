
class jaccard_similarity:
	def __init__(self, n_gram = 2):
		self.n_gram = 2

		

	def get_score(self, writer, ref):
		ref_n_gram = set(ref[index : index + self.n_gram] for index in range(0 , len(ref) - self.n_gram + 1))
		writer_n_gram = set(writer[index : index + self.n_gram] for index in range(0 , len(writer) - self.n_gram + 1))

		intersection = ref_n_gram.intersection(writer_n_gram)
		union = ref_n_gram.union(writer_n_gram)
		
		jaccard__similarity = len(intersection) / len(union)
		return  jaccard__similarity

