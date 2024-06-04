import statsmodels.api as sm

import pandas

from patsy import dmatrices

import tushare as ts
import pandas as pd


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


pro = ts.pro_api('f9d25f4ab3f0abe5e04fdf76c32e8c8a5cc94e384774da025098ec6e')




kk=pd.read_excel(r'C:\Users\徐浩然\Desktop\Eco_Final\added.xlsx',sheet_name='Sheet1')
#
#
stocks_codes = list(kk['Code'])
#
#
#


blank=pro.query('fina_indicator', ts_code='600000.SH',  period='20221231')


for i in stocks_codes:
    # df = pro.fina_indicator(ts_code='600000.SH')
    df = pro.query('fina_indicator', ts_code=i, period='20221231')
    df=df.iloc[:1,:]
    print(df)
    blank = pd.concat([blank, df], axis=0)


print(blank)
blank.to_excel(r'C:\Users\徐浩然\Desktop\fin_data2022.xlsx')

#
#
#



#
#
#
# startdate='20220101'
# enddate='20221231'
#
# def get_price():
#     price=pd.DataFrame()
#     for i in range(len(stocks_codes)):
#         k = pro.daily(ts_code=stocks_codes[i],start_date=startdate,end_date=enddate)
#         k.sort_values(by="trade_date", ascending=True, inplace=True)
#         print(k)
#         k = k[['vol']]
#         price["%s" % stocks_codes[i]] = k
#     return price
# prices=get_price()
# print(prices)
#
# prices.to_excel(r'C:\Users\徐浩然\Desktop\vol2022.xlsx')