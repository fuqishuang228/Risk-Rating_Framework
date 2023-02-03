import numpy as np
import pandas as pd
import math
from pandas import DataFrame

Transaction_Info = pd.read_csv('../data/Transaction_Information.csv')
Account_Info = pd.read_csv('../data/Account_Information.csv')
Life_Info=pd.read_csv('./cal_score/score_results/account_frequency.csv')
nodes = Account_Info["node"]
#node_label = Account_Info["label"]
edges = Transaction_Info["Tx_id"]
payer = Transaction_Info['index_from']
payee = Transaction_Info['index_to']
payer_life_span=Life_Info["out_life_span"]
payee_life_span=Life_Info["in_life_span"]
max_payer_life_span=max(payer_life_span)
max_payee_life_span=max(payee_life_span)
print(max_payee_life_span)
print(max_payer_life_span)

score1 = dict()
score2 = dict()
fw = open("./cal_score/score_results/score_life_span.csv", "w")
fw.write("Tx_id,score_frequency,\n")

for edge in edges:
    if payer_life_span[payer[edge]]==0:
        a=-1
    else:
        a=(2 * math.log(payer_life_span[payer[edge]], 10)-math.log(max_payer_life_span, 10)) / math.log(max_payer_life_span, 10)

    if payee_life_span[payee[edge]] ==0:
        b=-1
    else:
        b= (2 * math.log(payee_life_span[payee[edge]], 10) - math.log(max_payee_life_span, 10)) / math.log(max_payee_life_span, 10)
        # score[edge] =((2 * math.log(payer_life_span[payer[edge]], 10)-math.log(max_payer_life_span, 10)) / math.log(max_payer_life_span, 10)+( 2 * math.log(payee_life_span[payee[edge]], 10)-math.log(max_payee_life_span, 10)) / math.log(max_payee_life_span, 10))*1/2
    score2[edge]=(a+b)*0.5

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

