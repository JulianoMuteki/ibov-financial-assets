# ibov-financial-assets

## Web Scraping API Ibovespa

### Testing
- python3 api-screping.py
- curl http://127.0.0.1:5000/data?string_param=TAEE11


## Web API yfinance lib

### Testing
- python3 api-yahoo.py
- curl http://127.0.0.1:5000/history?ticker=TAEE11.SA&dateFilter=1d
- curl http://127.0.0.1:5000/info?ticker=TAEE11.SA

Note: 'dataGranularity': '1h', 'range': '1wk', 'validRanges': ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

### Docker
 - cd ibov-financial-assets/api-yahoo-market
 - docker build -t yfinance-api:v1 .
 - docker run --rm -p 5001:5001 --name yfinance-api yfinance-api:v1
