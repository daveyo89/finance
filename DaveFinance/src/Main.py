from DaveFinance.src.DataCollect.StockPriceData import GetStockPriceInfo
from DaveFinance.src.DataCollect.DataGather import DataGather
import pandas as pd


# TODO: tickers list will come from  best-index or a worth-of-it index.
class Main:

    def __init__(self):
        pass


portfolio = str(input("Give portfolio name/csv name"))
# # List portfolios here.
df = pd.read_csv(f"Portfolio/portfolios/{portfolio}.csv")
# #
tickers2 = (list(df["Symbol"]))
#
# # start_date = DataGather.get_year_from_today(1)
# # end_date = DataGather.get_year_from_today(0) # Leave blank for defaults = Get all available data.

# portfolio, portfolio_name = DataGather.portfolio_builder()  # Get portfolio name and tickers.
# DataGather.get_tickers(portfolio, portfolio_name)
#
GetStockPriceInfo(tickers2, portfolio).get_historical_price()
# DataGather.get_tickers()


