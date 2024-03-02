# ibov-financial-assets

## Web Scraping API Ibovespa

### Testing
- python3 api-screping.py
- curl http://127.0.0.1:5000/data?string_param=TAEE11


## Web API yfinance lib

### Testing with Python
- python3 api-yahoo.py
- curl http://127.0.0.1:5001/history?ticker=TAEE11.SA&periodFilter=6mo&intervalFilter=1mo
- curl http://127.0.0.1:5001/info?ticker=TAEE11.SA

Note: 'dataGranularity': '1h', 'range': '1wk', 'validRanges': ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

- period: As seen before, especially useful is the value “max”. The following are the valid values: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max.
- interval: Defines the size of each bar. Smaller bar sizes have more strict limitations, and only 7 days of 1-minute data can be retrieved. The following are the valid
- values: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

### Docker
 - cd ibov-financial-assets/api-yahoo-market
 - docker build -t yfinance-api:v1 .
 - docker run --rm -p 5001:5001 --name yfinance-api yfinance-api:v1

### Testing API api-yahoo-market
 - curl http://localhost:5001/info?ticker=TAEE11.SA

# Read more
 - https://pypi.org/project/yfinance/