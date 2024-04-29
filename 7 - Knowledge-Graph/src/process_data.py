import pandas as pd
from extract_detail import get_relation
from extract_detail import get_entities
from tqdm import tqdm


def process_data(data, col):
  graph_data = []
  print("extract object and subject ....")
  for element in tqdm(data[col]):
    graph_data.append(get_entities(element))

  relation = []
  print("extract relation ....")
  for element in tqdm(data[col]):
    relation.append(get_relation(element))  
  source = [i["Subject"] for i in graph_data]
  target = [i["object"] for i in graph_data]
  df = pd.DataFrame({
      "source" : source,
      "target" : target,
      "edge" :   relation
  })
  return df
