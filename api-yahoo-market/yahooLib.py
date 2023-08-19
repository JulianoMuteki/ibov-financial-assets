# Importando a biblioteca yfinance
import yfinance as yf

def get_Info(ticker):
    tickerObj = yf.Ticker(ticker)
    info =tickerObj.info
    return info

def get_History(ticker, periodFilter, intervalFilter):
    tickerObj = yf.Ticker(ticker)
    hist = tickerObj.history(period=periodFilter, interval=intervalFilter)

    hist.reset_index(inplace=True)
    hist['Date'] = hist['Date'].dt.strftime('%Y-%m-%d')
    hist.to_dict(orient='records')

    return hist.to_json()