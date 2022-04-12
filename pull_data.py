import yfinance as yf
import re
from csv import *
from datetime import date

tickers = ['msft', 'aapl', 'twtr', 'intc', 'goog', 'amzn', 'fb', 'nvda']

for ticker in tickers:
    data = yf.Ticker(ticker)
    end_date = date.today().strftime("%Y-%m-%d")
    start_date = date.today().strftime("-%m-%d")

    company = re.sub(r'[^\w\s]', ' ', data.info['longName']).split(" ")[0]

    yearly = data.history(start=str(int(date.today().strftime("%Y")) - 1)+start_date, end=end_date)
    yearly.insert(loc=0, column="Company", value=company, allow_duplicates=True)
    print(yearly.head(5))
    yearly.to_csv('C:\\Users\\Victor\\coding_projects\\python_projects\\data_analytic\\stock_csvs\\' + ticker + '.csv')