import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_colwidth', 200)


def create_graph_all(df, name = "ex_all.png"):
  G=nx.from_pandas_edgelist(df, "source", "target", 
                          edge_attr=True, create_using=nx.MultiDiGraph())
  plt.figure(figsize=(12,12))
  pos = nx.spring_layout(G)
  nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
  plt.savefig(name)


def create_graph_special(df, k = 0.5, rel = None,  name = "ex_all.png"):
  G=nx.from_pandas_edgelist(df[df['edge']==rel], "source", "target", 
                          edge_attr=True, create_using=nx.MultiDiGraph())
  plt.figure(figsize=(12,12))
  pos = nx.spring_layout(G)
  nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
  plt.savefig(name)
