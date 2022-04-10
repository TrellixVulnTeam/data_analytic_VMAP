import yfinance as yf
from csv import *
from datetime import date

tickers = ['msft', 'aapl', 'twtr', 'intc', 'tsm', 'goog', 'amzn', 'fb', 'nvda']

for ticker in tickers:
    data = yf.Ticker(ticker)
    end_date = date.today().strftime("%Y-%m-%d")
    start_date = date.today().strftime("-%m-%d")
    yearly = data.history(start=str(int(date.today().strftime("%Y")) - 1)+start_date, end=end_date)
    yearly.insert(loc=0, column="Stock Symbol", value=ticker, allow_duplicates=True)
    print(yearly.head())
    print(type(yearly))
    yearly.to_csv(ticker + '.csv')