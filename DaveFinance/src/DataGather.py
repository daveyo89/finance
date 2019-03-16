import pandas as pd
import glob
import os
import datetime as dt
from dateutil.relativedelta import relativedelta


def generate_portfolio(data_frame):
    """Choose from available categories.
    :return choices list.
    """
    df = data_frame

    options = list(enumerate(list(df.Sector.unique())))
    choices = []

    for e, x in options:
        print(f'{e}: {x}')

    choice = input().replace(" ", "").split(",")

    for c in choice:
        if options[int(c)][1] != "nan":
            choices.append(options[int(c)][1])
    return choices


def portfolio_builder():
    """Custom portfolio builder for singular tickets."""
    try:
        portfolio_name = str(input("Portfolio name: \n").replace(" ", ""))
        portfolio = set(input("Give comma separated tickers:\n").upper().replace(" ", "").split(","))

    except Exception as e:
        portfolio_name = "custom_portfolio"
        portfolio = ["TSLA"]
        print(str(e))

    return portfolio, portfolio_name


def get_year_from_today(year):
    dates = (dt.datetime.now() - relativedelta(years=year)).date()
    return [int(date) for date in ",".join([dates.strftime("%Y,%m,%d")]).split(",")]


class DataGather:
    """
    Data gathering.
    """

    def __init__(self):
        self.df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('../Data/Market_Tickers/', "*.csv"))))
        self.df = self.df.loc[:, ~self.df.columns.str.match('Unnamed')]
        self.df['Sector'].fillna("Unknown", inplace=True)
        os.makedirs("../Data/Portfolio", exist_ok=True)
        os.makedirs("../Data/Portfolio/all", exist_ok=True)
        os.makedirs("../Data/Portfolio/custom", exist_ok=True)
        os.makedirs("../Data/Portfolio/categorical", exist_ok=True)

    def all_market_tickers(self):
        """Saves every ticker from available markets
        :return pandasDataFrame
        """
        df = self.df
        df.to_csv(f"../Data/Portfolio/all/all_tickers.csv",
                  sep=',', encoding='utf-8', mode='w', index=False, header=True)
        return df

    def category_tickers(self):
        """Use generate_portfolio to get viable list for categorical portfolio building."""
        df = self.df
        categories = generate_portfolio(df)
        df = df.loc[df['Sector'].isin(categories)]
        pf_name = [s[:2] for s in categories]
        df.to_csv(f"../Data/Portfolio/categorical/{''.join(pf_name)}.csv",
                  sep=',', encoding='utf-8', mode='w', index=False, header=True)
        return df

    def get_custom_tickers(self):
        """Get all ticker symbols from previously downloaded csv-s and put them in tickers.csv"""
        portfolio, portfolio_name = portfolio_builder()
        df = self.df
        df = df.loc[df["Symbol"].isin(portfolio)]
        # df.set_index("Symbol", inplace=True)
        # df.insert(loc=0, column='Symbol', value=df.index)
        try:
            df.to_csv(f"../Data/Portfolio/custom/{''.join(portfolio_name)}.csv",
                      sep=',', encoding='utf-8', mode='w', index=False, header=True)
        except KeyError as ke:
            print(str(ke))
        return df, portfolio_name
