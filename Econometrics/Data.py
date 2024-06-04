import pandas as pd

# 创建示例数据
data = pd.read_excel(r'C:\Users\徐浩然\Desktop\000300cons.xls',sheet_name='Sheet1')

data['Code'] = data['Code'].astype(str).str.zfill(6)


data['交易所Exchange'] = data['交易所Exchange'].astype(str)
#
df = data
#
# 添加后缀
df['Code'] = df.apply(lambda row: row['Code'] + '.SZ' if row['交易所Exchange'] == '深圳证券交易所' else row['Code'] + '.SH', axis=1)
df.to_excel(r'C:\Users\徐浩然\Desktop\added.xlsx')
# 打印结果
print(df)
