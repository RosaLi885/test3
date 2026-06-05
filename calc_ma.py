import pandas as pd

# 读取数据
df = pd.read_csv('stock_data.csv')

# Bug 1: 列名写错了（应该是 'close'，这里写了 'Close'）
df['ma5'] = df['Close'].rolling(window=5).mean()

# Bug 2: 窗口大小写成了字符串 '10'
df['ma10'] = df['close'].rolling(window='10').mean()

# Bug 3: 保存时忘了指定 index=False，导致多出一列 Unnamed
df.to_csv('output.csv')

print("Done!")
