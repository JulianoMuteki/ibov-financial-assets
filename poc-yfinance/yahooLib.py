import yfinance as yf

msft = yf.Ticker("MSFT")

df = msft.history(period="1y", interval="1mo")

#df = tickers.tickers.AAPL.history(period="1mo")
df.reset_index(inplace=True)
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
#df.drop(['Dividends','Stock Splits'], inplace=True, axis=1)
df.to_dict(orient='records')


# get stock info
print(df)
# msft.dividends

# get historical market data
# hist = msft.history(period="1mo")

# show meta information about the history (requires history() to be called first)
# msft.history_metadata

# print(msft.history_metadata)