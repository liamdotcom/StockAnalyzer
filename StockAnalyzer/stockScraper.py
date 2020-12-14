import datetime
import pandas as pd
import time

import requests
from bs4 import BeautifulSoup as soup


def getPrice(ticker):
    my_url = 'http://finance.yahoo.com/quote/' + ticker + '?p=' + ticker
    r = requests.get(my_url)
    page_soup = soup(r.text, "lxml")
    price = page_soup.find_all('div', {'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price


def startScrape(ticker):
    for step in range(1, 10000):
        price = []
        col = []
        time_stamp = datetime.datetime.now()
        time_stamp = time_stamp.strftime("%Y-%m-%d %H:%m:%S")
        price.append(getPrice(ticker))
        col = [time_stamp]
        col.extend(price)
        df = pd.DataFrame(col)
        df = df.T
        df.to_csv("stock_data.csv", mode='a', header=False)
        print(col)
        time.sleep(15)

