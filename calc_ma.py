import pandas as pd

# 读取数据
df = pd.read_csv('sample.csv')

# 修复 Bug 1: 列名应该是 'close' 而不是 'Close'
df['ma5'] = df['close'].rolling(window=5).mean()

# 修复 Bug 2: 窗口大小必须是整数，而不是字符串
df['ma10'] = df['close'].rolling(window=10).mean()

# 修复 Bug 3: 保存时需要指定 index=False，避免多出一列 Unnamed
df.to_csv('output.csv', index=False)

print("Done!")
