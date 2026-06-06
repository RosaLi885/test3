import pandas as pd
import numpy as np

# 读取数据
df = pd.read_csv('stock_data.csv')
df['date'] = pd.to_datetime(df['date'])

# 计算移动平均线
df['MA5'] = df['close'].rolling(5).mean()
df['MA10'] = df['close'].rolling(10).mean()
df['MA20'] = df['close'].rolling(20).mean()

# 查看最新数据
print("最新数据：")
print(df[['date', 'close', 'MA5', 'MA10', 'MA20']].tail())

# 保存结果到新文件
df.to_csv('stock_data_with_ma.csv', index=False)
print("\n已保存到 stock_data_with_ma.csv")
