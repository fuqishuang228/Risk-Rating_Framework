
import numpy as np
import pandas as pd


Account_Info = pd.read_csv('../data/Account_Information.csv')
all_Tx_Num=Account_Info['all_degree']
Tx_Acc_Num=Account_Info['Tx_Acc_Num']

wash_freq=dict()
I=len(all_Tx_Num)



fw = open("./cal_score/score_results/Acc_wash_freq.csv", "w")
fw.write("Tx_id,Acc_wash_freq\n")


for i in range(0,I):
    wash_freq[i]=1.0*all_Tx_Num[i]/Tx_Acc_Num[i]

    fw.write("%s,%s\n" % (str(i), str(wash_freq[i])))
fw.close()


