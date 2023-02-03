import numpy as np
import pandas as pd
import math
from pandas import DataFrame

Transaction_Info = pd.read_csv('../data/Transaction_Information.csv')
Account_Info = pd.read_csv('../data/Account_Information.csv')

Payer_TxNumber = Account_Info["out_degree"]
Payee_TxNumber = Account_Info["in_degree"]
max_Payee_TxNumber =max(Payee_TxNumber)
max_Payer_TxNumber =max(Payer_TxNumber)


nodes = Account_Info["node"]
#node_label = Account_Info["label"]
edges = Transaction_Info["Tx_id"]
payer = Transaction_Info['index_from']
payee = Transaction_Info['index_to']
time=Transaction_Info["timestamp"]
score = dict()
payer_life_span=dict()
payee_life_span=dict()
#Transaction_Info["timestamp"]=list(map(int,Transaction_Info["timestamp"].tolist()))


fw = open("./cal_score/score_results/account_frequency.csv", "w")
fw.write("index,out_life_span,in_life_span\n")
#----统计生命周期--------#
#得到payer对应的timestamp，然后找出最小和最大值，求差值,
for node in nodes:
    if Payer_TxNumber[node]==0:
        payer_life_span[node]=0
    else:
        timestamp1 = Transaction_Info.loc[payer == node]["timestamp"]
        min_t1 = min(timestamp1)
        max_t1 = max(timestamp1)
        payer_life_span[node] = float((max_t1 - min_t1) / (3600*24))# second change to day

    if Payee_TxNumber[node] == 0:
        payee_life_span[node] = 0
    else:
        timestamp2 = Transaction_Info.loc[payee == node]["timestamp"]
        min_t2 = min(timestamp2)
        max_t2 = max(timestamp2)
        payee_life_span[node] = float((max_t2 - min_t2) / (3600*24)) # second change to day

    fw.write("%s,%s,%s\n" % (str(node), str(payer_life_span[node]), str(payee_life_span[node])))
a=1
fw.close()