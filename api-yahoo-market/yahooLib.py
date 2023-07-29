# Importando a biblioteca yfinance
import yfinance as yf

def get_Info(ticker):
    tickerObj = yf.Ticker(ticker)
    info =tickerObj.info
    return info

def get_History(ticker, dateFilter):
    tickerObj = yf.Ticker(ticker)
    hist = tickerObj.history(period=dateFilter)
    return hist.to_json()

