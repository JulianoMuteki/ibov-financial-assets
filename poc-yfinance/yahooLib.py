import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
#print(msft.info)
# msft.dividends

# get historical market data
hist = msft.history(period="1mo")

# show meta information about the history (requires history() to be called first)
msft.history_metadata

print(msft.history_metadata)