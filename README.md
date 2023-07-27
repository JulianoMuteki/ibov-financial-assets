# ibov-financial-assets

## Web Scraping API Ibovespa

### Testing
- python3 api-screping.py
- curl http://127.0.0.1:5000/data?string_param=TAEE11


## Web Scraping API yfinance lib

### Testing
- python3 api-yahoo.py
- curl http://127.0.0.1:5000/history?string_param=1mo
- curl http://127.0.0.1:5000/history?string_param=max
- curl http://127.0.0.1:5000/info

Note: 'dataGranularity': '1h', 'range': '1wk', 'validRanges': ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
