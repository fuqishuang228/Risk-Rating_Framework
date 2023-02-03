## A General Framework for Account Risk Rating on Ethereum

## 1.English Version

Dataset Discription
(1) Dataset Name:
	Account Risk Dataset on Ethereum

(2) Description  
	Our work shares phishing account information from Etherscan. In addition, we share the RiskPro algorithm for detection in our work (RiskProp: Account Risk Rating on Ethereum via De-anonymous Score and Network Propagation).  
    We crawled the phishing accounts in Ethereum from December 1, 2019 to December 31, 2019 and their first-order and second-order nodes from https://etherscan.io/accounts/label/phish-hack, and got a total of 243 phishing accounts. The transaction network  consists of  1.19 million accounts and 4.13 million transactions.

(3) Update Log
	We crawled the phishing accounts in Ethereum from December 1, 2019 to December 31, 2019 

(4) Contents
    Due to GitHub's file size limit, see other data files in the OneDrive sharing page:
    https://www.dropbox.com/scl/fo/naxj68ft8zbl0ssry6128/h?dl=0&rlkey=53tqxfjfs6mtc1cwxnty7okv5

	a. 803_Accounts_Labels.csv
	Discription: this file contains 803 accounts who have labels.

	-Column：
		1. index：index of account
		2. Address: address of account
		3. discription: description of  account type
		4. label: label of account e.g., label of illicit account is 1, label of licit account is 0.
		sum：4 columns
	-Row：
		each row represents an account.
	
	b. Account_Information.csv
	-Column：
		1. node: index of account
        2. address: address of account
		3. out_degree: payments number of account
		4. in_degree: receptions number of account
		5. all_degree: transaction number of account
        6. Tx_Acc_Num: number of accounts traded on account
        7. Acc_wash_freq: wash frequency of account
		8. label: label of account
		sum：8 columns
	-Row：
		each row represents an account.


	c. Transaction_Information.csv
	-Column：
		1. Tx_id: index of transaction
		2. address_from: address of payer
		3. address_to: address of payee
		4. index_from: index of payer
		5. index_to: index of payee
        6. timestamp: transaction time
        7. value: ETH amount of transaction
        8. score_anonymy: anony_suspic of transaction
        9. score_life_span: lfsp_suspic of transaction
        10. score_wash: wash_suspic of transaction
		sum：10 columns
	-Row：
		each row represents a transaction.
	


(5) Citation
	updating...
	BibTex
	IEEE
	ACM
(6) Contact
	updating...
	Please contact  () for any questions about the dataset

Code Discription
(1)Requirements
To run this code fully, you will need these repositories. We have been running our code in Python 3.7.
	numpy == 1.21.2
	pandas == 1.3.5

(2)Contents
    	
		--Folder1:Score_Calculation
    	In folder1, there are some code file to help calculate 3 kind of suspiciousness.
    
    	1)lfspan_susp:
        a. cal_acc_lifespan.py
		This script will calculate account lifespan with the account information and transaction information.

	    b. cal_score_lfspan.py
		This script will calculate lfspan_suspic of transactions with the transaction information and account lifespan information.

    2)wash_susp:
        a. cal_Tx_number_per_acc.py
		This script will calculate number of accounts traded on account with the account information and transaction information.

	    b. cal_wash.py
		This script will calculate wash frequency of account with the transaction information and number of accounts traded on account.

	    c. cal_score_wash.py
		This script will calculate wash_suspic of transactions with the transaction information and account wash frequeny.

    3)anonymy_susp:
        a. cal_score_anonymy.py
		This script will calculate anonymy_suspic of transactions with the transaction information and account information.

    --Folder2:Risk_Rating
    In folder2, there are some code file to rate account risk with 3 kinds of suspiciousness metrics reapectively.

    1)Score_Lifespan_Risk_Rating.py
    This script will calculate risk of accounts with our risk rating method of lfspn_suspic.

    2)Score_Wash_Risk_Rating.py
    This script will calculate risk of accounts with our risk rating method of wash_suspic.

    3)Score_Anony_Risk_Rating.py
    This script will calculate risk of accounts with our risk rating method of anonymy_suspic.
    
===============================================================================================================================================

## 2.中文版

数据集信息
(1) 名称：
	以太坊账户风险数据集

(2) 简介：

	a. 数据来源：从 https://etherscan.io 爬取了到的目标节点相关交易数据. 
	b. 数据研究对象：以太坊
	c. 数据集大小：该二阶交易网络数据集为从Etherscan上爬取的243个目标钓鱼节点以及560个非钓鱼节点的二阶交易网络信息。由于内存受限，选择了和一阶节点发生的最近的交易中的10个账户，并将这10个账户的一阶邻居作为二阶节点。在该二阶交易网络中有119万个账户和414万条交易。
	d. 研究工作：《A General Framework for Account Risk Rating on Ethereum: Towards Safer Blockchain Technology》

(3) 更新时间：

	数据集是从2019年12月1日到2019年12月31日目标账户最近的10000条交易数据（若不足10000条则统计全部交易）

(4) 内容：
    由于github内存有限，我们将数据文件放在了onedrive中，读者可下载:
	https://www.dropbox.com/scl/fo/naxj68ft8zbl0ssry6128/h?dl=0&rlkey=53tqxfjfs6mtc1cwxnty7okv5

	a. 803_Accounts_Labels.csv
	描述：该文件包含了训练集和测试集的账户信息，用于实验结果验证。
	
	-列：
		1. node：账户的序号
		2. Address: 账户的地址
		3. discription: 账户的类型描述
		4. label:账户的标签，非法账户的标签为1，正常账户的标签为0。
		总和：4列
	-行：
		每一行代表一个账户信息
	
	b. Account_Information.csv
	列：
		1. node: 账户的序号
        2. Address: 账户的地址
		3. out_degree: 账户的转账次数
		4. in_degree: 账户的入账次数
		5. all_degree: 账户的交易次数
        6. Tx_Acc_Num: 账户交易的账户数量
        7. Acc_wash_freq: 账户刷量频率
		8. label: 账户的标签
        总和：8列
	-行：
		每一行代表一个账户信息
	
	c.Transaction_Information.csv
	-列：
		1. Tx_id：交易的序号
		2. address_from: 转账账户的地址
		3. address_to: 入账账户的地址
		4. index_from: 转账账户的序号
		5. index_to: 入账账户的序号
        6. timestamp：交易时间
        7. value: 交易的ETH金额
		8. score_anonymy: 交易的匿名分数
		9. score_life_span: 交易的生命周期分数
        10.score_wash: 交易的刷量分数
		总和：10列
	-行：
		每一行代表一次交易信息
	


代码信息
(1)Requirements
我们使用Python3.7以及下面两个第三方库：
	numpy == 1.21.2
	pandas == 1.3.5

(2)内容
    --文件夹1：Score_Calculation
    文件夹1中的文件是帮助计算三种可疑度指标的值的。
    Folder1:Score_Calculation
    In folder1, there are some code file to help calculate 3 kind of suspiciousness.

    1)lfspan_susp:
        a. cal_acc_lifespan.py 
        这个代码文件输入了账户信息和交易信息，计算账户的生命周期。
	
	    b. cal_score_lfspan.py
		这个代码文件输入交易信息和账户生命周期，计算交易的lfsp_suspic。

    2)wash_susp:
        a. cal_Tx_number_per_acc.py 
        这个代码文件输入了账户信息和交易信息，计算账户交易和一个账户的平均交易数量。

        b. cal_wash.py
        这个代码文件输入账户信息和账和一个账户的平均交易数量，计算账户的刷量频率。

        b. cal_score_wash.py
        这个代码文件输入交易信息和账和一个账户的平均交易数量，计算交易的wash_suspic。

    3)anonymy_susp:
        a. cal_score_anonymy.py
        这个代码文件输入交易信息和账户交易数量，计算交易的anonymy_suspic。

    --文件夹2：Risk_Rating
    文件夹2中的文件是使用三种可疑度指标的风险评估代码。

    1）Score_Lifespan_Risk_Rating.py
        输入账户信息和交易信息，使用lfsp_suspic以及风险评估框架去评估账户风险，最后输出账户和交易的指标值。

    2）Score_Wash_Risk_Rating.py
        输入账户信息和交易信息，使用wash_suspic以及风险评估框架去评估账户风险，最后输出账户和交易的指标值。

    3）Score_Anony_Risk_Rating.py
        输入账户信息和交易信息，使用anonymy_suspic以及风险评估框架去评估账户风险，最后输出账户和交易的指标值。
