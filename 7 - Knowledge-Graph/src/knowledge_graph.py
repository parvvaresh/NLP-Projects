from process_data import process_data
from make_graph import create_graph_all, create_graph_special

class knowledge_graph:
	def __init__(self, data, col):
		self.df = process_data(data, col = "sentence")

	def get_all_relation(self, name):
		create_graph_all(self.df, name = name)

	def get_with_relation(self, rel, name):
		create_graph_special(self.df, k = 0.5, rel = rel,  name = name)
