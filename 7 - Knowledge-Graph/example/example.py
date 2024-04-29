import pandas as pd
from knowledge_graph import knowledge_graph

data = pd.read_csv("wiki_sentences_v2.csv")

kg = knowledge_graph(data, "sentence")
kg.get_all_relation("example_1.png")
kg.get_with_relation(rel = "composed by",  name = "example_2.png")
kg.get_with_relation(rel = "written by", name =  "example_3.png")
kg.get_with_relation(rel = "released in", name =  "example_4.png")
