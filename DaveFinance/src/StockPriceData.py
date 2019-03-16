import datetime as dt
import pandas_datareader.data as web
import os
from tqdm import tqdm


class GetStockPriceInfo:
    """Get detailed stock price info"""

    def __init__(self, tickers: list, portfolio_name, start=None, end=None):
        self.tickers = tickers
        self.start = start
        self.end = end
        self.portfolio_name = portfolio_name
        self.stock_data_path = "../Data/stock_data"

        os.makedirs(self.stock_data_path, exist_ok=True)
        os.makedirs(f"{self.stock_data_path}/{portfolio_name}", exist_ok=True)

    def __repr__(self):
        return f"""Get historical data for {self.tickers} stocks."""

    def get_historical_price(self):
        if self.start:
            self.start = dt.datetime(self.start[0], self.start[1], self.start[2])
        if self.end:
            self.end = dt.datetime(self.end[0], self.end[1], self.end[2])

        print(f'Getting info for {self.tickers} - {self.start if self.start else "default date to "}'
              f'{"" if self.end else "default date."}')
        for ticker in tqdm(self.tickers):
            try:
                df = web.DataReader(ticker, 'yahoo', self.start, self.end)
                df.reset_index(inplace=True)
                df.set_index("Date", inplace=True)
                df.sort_index(inplace=True)

                df.to_csv(f'{self.stock_data_path}/{self.portfolio_name}/{ticker}.csv')
            except KeyError as e:
                print(f"{str(e)} key error, date range might be too far back.\n")
                continue
            except Exception as e:
                print(f"Couldn't get {ticker} info. Error: {str(e)}\n")
                continue
