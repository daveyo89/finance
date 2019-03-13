import pandas as pd
import glob
import os
import datetime as dt
from dateutil.relativedelta import relativedelta


class DataGather:
    """
    Data gathering.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_tickers(portfolio=None, portfolio_name="all_tickers"):
        """Get all ticker symbols from previously downloaded csv-s and put them in tickers.csv"""
        os.makedirs("Portfolio", exist_ok=True)
        os.makedirs("Portfolio/portfolios", exist_ok=True)
        path = f"Portfolio/portfolios/{portfolio_name}.csv"

        df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('all_tickers/', "*.csv"))))
        df.set_index("Symbol", inplace=True)
        df.insert(loc=0, column='Symbol', value=df.index)
        if portfolio is not None:
            try:
                df.loc[portfolio].to_csv(path, sep=',', encoding='utf-8', mode='w', index=False, header=True)
            except KeyError as ke:
                print(str(ke))

        else:
            df.to_csv(path, sep=',', encoding='utf-8', mode='w', index=False, header=True)
        # Use this method from Main.py

    @staticmethod
    def portfolio_builder(portfolio_name="tickers", portfolio=None):
        try:
            portfolio_name = str(input("Portfolio name: \n").replace(" ", ""))
            portfolio = set(input("Give comma separated tickers:\n").upper().replace(" ", "").split(","))
            if len(portfolio) <= 1 and portfolio == "":
                portfolio = None
            if len(portfolio_name) == 0:
                portfolio_name = "all_tickers"
            print(f"portfolio: {portfolio}")
            print(f"portfolio name: {portfolio_name}")
        except Exception as e:
            print(str(e))
        return portfolio, portfolio_name

    @staticmethod
    def get_year_from_today(year):
        dates = (dt.datetime.now() - relativedelta(years=year)).date()
        return [int(date) for date in ",".join([dates.strftime("%Y,%m,%d")]).split(",")]
