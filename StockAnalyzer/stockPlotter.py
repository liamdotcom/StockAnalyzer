import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import accountBackTest
from matplotlib import style
import os

os.environ['indicate'] = '0'

def startPlot():
    account = accountBackTest.Account()
    style.use('fivethirtyeight')
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(2, 1, 1)
    indicators = fig.add_subplot(2, 1, 2)

    def animate(i):
        df = pd.read_csv('stock_data.csv')
        ys = df.iloc[1:, 2].values
        xs = list(range(1, len(ys)+1))
        current = str(df.iloc[-1:, 2].values)
        ax.clear()
        ax.plot(xs, ys, label='Stock Price', color='blue')
        ax.set_title("Stock Analyzer Current Price:"+current, fontsize=16)
        ax.legend(loc='upper left')

        shortEMA = df.iloc[1:, 2].ewm(span=12, adjust=False).mean()
        longEMA = df.iloc[1:, 2].ewm(span=26, adjust=False).mean()
        MACD = shortEMA - longEMA
        signal = MACD.ewm(span=9, adjust=False).mean()
        xsMACD = list(range(1, len(MACD) + 1))
        xsSignal = list(range(1, len(signal) + 1))
        indicators.clear()
        indicators.plot(xsMACD, MACD, label='MACD', color='red')
        indicators.plot(xsSignal, signal, label='Signal', color='green')
        indicators.legend(loc='upper left')
        if len(MACD) > 1:
            if MACD.loc[len(MACD)] > signal.loc[len(MACD)]:
                if os.getenv('indicate') == '0':
                    os.environ['indicate'] = '1'
                    print("Buy Signal: " + current)
                    if len(MACD) > 18:
                        account.buyShares(df.iloc[-1:, 2].values)
            if MACD.loc[len(MACD)] < signal.loc[len(MACD)]:
                if os.getenv('indicate') == '1':
                    os.environ['indicate'] = '0'
                    print("Sell Signal: " + current)
                    if len(MACD) > 18:
                        account.sellShares(df.iloc[-1:, 2].values)


    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
