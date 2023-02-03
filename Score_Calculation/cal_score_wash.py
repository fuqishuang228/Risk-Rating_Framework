import numpy as np
import pandas as pd
import math
from pandas import DataFrame

Transaction_Info = pd.read_csv('../data/Transaction_Information.csv')
Account_Info = pd.read_csv('../data/Account_Information.csv')

nodes = Account_Info["node"]
edges = Transaction_Info["Tx_id"]
payer = Transaction_Info['index_from']
payee = Transaction_Info['index_to']

payer_wash_freq=Account_Info["Acc_wash_freq"]
payee_wash_freq=Account_Info["Acc_wash_freq"]

Max_wash_freq=max(Account_Info["Acc_wash_freq"])
print(Max_wash_freq)
score1 = dict()

fw = open("./cal_score/score_results/score_wash.csv", "w")
fw.write("Tx_id,score_wash,\n")
x=2
for edge in edges:

    score1[edge] =((x-2 * math.log(payer_wash_freq[payer[edge]],10)) / x+( x-2 * math.log(payee_wash_freq[payee[edge]],10)) / x)*1/2
    if score1[edge] > 1:
        score1[edge] = 1
    if score1[edge] < -1:
        score1[edge] = -1


    fw.write("%s,%s\n" % (str(edge), str(score1[edge])))
fw.close()

