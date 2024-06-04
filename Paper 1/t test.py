from scipy import stats
import numpy as np
import pandas as pd

Bond=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\HE.xlsx', sheet_name='Bond',index_col=0,parse_dates=[0])
Oil=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\HE.xlsx', sheet_name='Oil',index_col=0,parse_dates=[0])
BTC=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\HE.xlsx', sheet_name='BTC',index_col=0,parse_dates=[0])
Gold=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\HE.xlsx', sheet_name='Gold',index_col=0,parse_dates=[0])

Bonds=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\HE.xlsx', sheet_name='Bond',index_col=0,parse_dates=[0])
Oils=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\HE.xlsx', sheet_name='Oil',index_col=0,parse_dates=[0])
BTCs=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\HE.xlsx', sheet_name='BTC',index_col=0,parse_dates=[0])
Golds=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\HE.xlsx', sheet_name='Gold',index_col=0,parse_dates=[0])



HBond=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Hedge_HE.xlsx', sheet_name='Bond',index_col=0,parse_dates=[0])
HOil=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Hedge_HE.xlsx', sheet_name='Oil',index_col=0,parse_dates=[0])
HBTC=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Hedge_HE.xlsx', sheet_name='BTC',index_col=0,parse_dates=[0])
HGold=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-China\Hedge_HE.xlsx', sheet_name='Gold',index_col=0,parse_dates=[0])

HBonds=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\Hedge_HE.xlsx', sheet_name='Bond',index_col=0,parse_dates=[0])
HOils=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\Hedge_HE.xlsx', sheet_name='Oil',index_col=0,parse_dates=[0])
HBTCs=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\Hedge_HE.xlsx', sheet_name='BTC',index_col=0,parse_dates=[0])
HGolds=pd.read_excel(r'C:\Users\徐浩然\Desktop\DCC-data-US\Hedge_HE.xlsx', sheet_name='Gold',index_col=0,parse_dates=[0])

# print(Bond)
for i in [2,4,0,1,3,5]:
   rt=HBTCs.iloc[:,i]
   r = stats.ttest_1samp(rt, 1)
   print("statistic:", round(r.__getattribute__("statistic"),3))
   print("pvalue:", round(r.__getattribute__("pvalue"),3))
