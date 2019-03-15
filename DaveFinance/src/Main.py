from DaveFinance.src.StockPriceData import GetStockPriceInfo
from DaveFinance.src.DataGather import *
# TODO: tickers list will come from  best-index or a worth-of-it index.


class Main:

    def __init__(self):

        pass

    # # start_date = DataGather.get_year_from_today(1)
    # # end_date = DataGather.get_year_from_today(0) # Leave blank for defaults = Get all available data.

    dg = DataGather()
    custom_ticks, name = dg.get_custom_tickers()
    #
    # portfolio, portfolio_name = DataGather.portfolio_builder()  # Get portfolio name and tickers.
    #
    # DataGather.get_tickers(portfolio, portfolio_name)
    # #
    # df = pd.read_csv(f"../Data/Portfolio/portfolios/{portfolio_name}.csv")
    #
    tickers2 = (list(custom_ticks["Symbol"]))
    print(tickers2)
    #
    # TODO: StockPriceDataban a ticker paramétert a portfoliobol akarom kivenni, nem pedig így átadni.
    # TODO: választhatóvá kell tenni ugyanugy mint a kategoriaknal.
    GetStockPriceInfo(tickers2, portfolio_name=name).get_historical_price()
    # #


Main()
