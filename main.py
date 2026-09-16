import oandapyV20 as oanda
import numpy as nump
import yfinance as yf

ticker = "XAUUSD"
yf.download(ticker)

ticker1 = "XAUUSD"
timeframe1 = "15m"

def get_data(ticker, timeframe):
    data = yf.download(ticker, interval=timeframe)
    return data

yf.download(ticker, period="15m", interval="1m")

historical = get_data(ticker1, timeframe1)

