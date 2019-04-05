from StockData import GetStockInfo
from DataGather import *

from pathlib import Path

formatters = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'END': '\033[0m',
}


def get_choice(options):
    options = list(enumerate(list(options)))
    for e, x in options:
        print(f'{e}: {x}')
    try:
        choice = int(input("Please select an option: "))
        if choice >= len(options) or choice < 0:
            return "Invalid argument!"
        return options[choice][1]
    except (TypeError, ValueError) as te:
        print(str(te))
        return "Invalid argument!"


def read_to_df(path):
    df = pd.read_csv(path)
    return list(df['Symbol'])


def list_portfolios(path='../Data/Portfolio'):
    options = [x.name for x in Path(os.path.join(os.getcwd(), path)).glob('*/')]
    return options


class Main:

    def __init__(self):
        pass

    def main(self):
        loop = True
        while loop:
            try:
                options = ["New Portfolio", "Get Stock Prices", "Exit"]
                choice = (get_choice(options=options))
                if choice == options[0]:
                    choice = get_choice(options=["Custom", "Category", "All", "Back"])
                    if choice == "Custom":
                        DataGather().get_custom_tickers()
                        continue
                    elif choice == "Category":
                        DataGather().category_tickers()
                        continue
                    elif choice == "All":
                        DataGather().all_market_tickers()
                        continue
                    elif choice == "Cancel":
                        continue

                elif choice == options[1]:
                    choice = get_choice(options=list_portfolios())
                    if choice == "all":
                        path = f"../Data/Portfolio/{choice}/all_tickers.csv"
                        tickers = read_to_df(path)
                        GetStockInfo(tickers, portfolio_name="all").get_historical_price()
                        continue
                    elif choice == "categorical":
                        path = f"../Data/Portfolio/{choice}/"
                        choice = get_choice(options=list_portfolios(path))
                        print(f"You chose: # {choice} #")
                        tickers = read_to_df(f"{path}/{choice}")
                        GetStockInfo(tickers=tickers, portfolio_name=choice).get_historical_price()
                        continue
                    elif choice == "custom":
                        path = f"../Data/Portfolio/{choice}/"
                        choice = get_choice(options=list_portfolios(path))
                        tickers = read_to_df(f"{path}/{choice}")
                        print(f"You chose: # {choice} #")
                        print(tickers)
                        GetStockInfo(tickers=tickers,
                                     portfolio_name=choice.replace('.csv', '')).get_historical_price()
                        continue

                elif choice == "Exit":
                    loop = False
                else:
                    continue

            except FileNotFoundError as e:
                print(f"{formatters['RED']}File not found, please build portfolio first!\n" + str(e)
                      + f"{formatters['END']}")


m = Main()
m.main()