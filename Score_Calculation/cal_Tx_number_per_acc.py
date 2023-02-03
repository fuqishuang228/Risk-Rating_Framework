import random
import subprocess
import numpy as np
# import torch
# from scipy import sparse
# import time
# from collections import defaultdict
# import csv
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import math
# from scipy.stats import pearsonr
from math import exp
import csv
import pickle

# import warnings
# warnings.filterwarnings("ignore")
beta1 = 1
beta2 = 1
Transaction_Info = pd.read_csv('../data/Transaction_Information.csv')
Account_Info = pd.read_csv('../data/Account_Information.csv')
edges= pd.read_csv('../data/Transaction_Information.csv',usecols=["index_from","index_to"])
edges=np.array(edges)
nodes=np.array(Account_Info['node'])
Nodes=Account_Info['node']
Edges=Transaction_Info["Tx_id"]

# all_hash=pd.read_csv('./data/all_hash_10_train.csv',names = ['index','address','label',"out_degree","in_degree","all_degree"])
# all_index=pd.read_csv('./data/all_index_adj_together_with_start_risk_with_count_with_all.csv')
# nodes = np.array(all_hash["index"])
# Nodes = all_hash["index"]
# #edges = all_index["Unnamed: 0"]
# edges = pd.read_csv('./data/all_index_adj_together_with_start_risk_with_count_with_all.csv',usecols=["index_from","index_to"])
# edges=np.array(edges)
# Edges = all_index["Unnamed: 0"]
print("ethereum network has %d nodes and %d edges" % (len(nodes), len(edges)))
G=nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
from_degree={}
to_degree={}
# for edge in Edges:
#     from_degree[edge]=G.degree[all_index['index_from'][edge]]
#     to_degree[edge]=G.degree[all_index['index_to'][edge]]
#
# fw = open("./results/smalldata_tofrom_degree.csv","w")
# fw.write("to_degree,from_degree\n")
#
# for edge in Edges:
#     fw.write("%s,%s\n" %(str(to_degree[edge]), str(from_degree[edge])))
# fw.close()

fw = open("./cal_score/score_results/Tx_Number_Per_Acc.csv","w")
fw.write("node,out_Num,in_Num,all_Num\n")

for node in Nodes:
    fw.write("%s,%s,%s,%s\n" %(str(node),str(G.out_degree[node]),str(G.in_degree[node]), str(G.degree[node])))
fw.close()

