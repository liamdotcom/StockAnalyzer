import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot()

df = pd.read_csv('stock_data.csv')
shortEMA = df.iloc[1:, 2].ewm(span=12, adjust=False).mean()
longEMA = df.iloc[1:, 2].ewm(span=26, adjust=False).mean()
MACD = shortEMA - longEMA
signal = MACD.ewm(span=9, adjust=False).mean()
xsMACD = list(range(1, len(MACD)+1))
xsSignal = list(range(1, len(signal)+1))

ax.plot(xsMACD, MACD, label='MACD', color='red')
ax.plot(xsSignal, signal, label='Signal', color='blue')
plt.show()
