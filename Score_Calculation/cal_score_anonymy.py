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
# node_label = Account_Info["label"]
edges = Transaction_Info["Tx_id"]
payer = Transaction_Info['index_from']
payee = Transaction_Info['index_to']

score1 = dict()
score2 = dict()
fw = open("./cal_score/score_results/score_anonymy.csv", "w")
fw.write("Tx_id,score_anonymy,\n")

for edge in edges:
    score2[edge] = -((2 * math.log(Payer_TxNumber[payer[edge]], 10) - math.log(max_Payer_TxNumber, 10)) / math.log(max_Payer_TxNumber, 10) + (2 * math.log(Payee_TxNumber[payee[edge]], 10) - math.log(max_Payee_TxNumber, 10)) / math.log(max_Payee_TxNumber, 10)) / 2

    # score1[edge] =((2 * payer_life_span[payer[edge]]-max_payer_life_span) / max_payer_life_span+( 2 * payee_life_span[payee[edge]]-max_payee_life_span) / max_payee_life_span)*1/2
    # if score1[edge] > 1:
    #     score1[edge] = 1
    # if score1[edge] < -1:
    #     score1[edge] = -1
    if score2[edge] > 1:
        score2[edge] = 1
    if score2[edge] < -1:
        score2[edge] = -1

    fw.write("%s,%s\n" % (str(edge), str(score2[edge])))
fw.close()
