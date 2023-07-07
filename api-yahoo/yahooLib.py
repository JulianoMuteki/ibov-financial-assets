# Importando a biblioteca yfinance
import yfinance as yf
import pandas as pd

# Ticker da Lockheed Martin na NYSE - LMT
lmt = yf.Ticker("LMT")
type(lmt)

# Informações do Ticker
# To do function 
#print(lmt.info)

# Obtendo o histórico completo da ação
# To do function 
# hist = lmt.history(period="max")
# print(hist)
def get_Info():
    info =lmt.info
    df = pd.DataFrame(info)
    return df.to_json()

def get_History(periodValue):
    hist = lmt.history(period=periodValue)
    df = pd.DataFrame(hist)
    return df.to_json()

