# pcost.py
#
# Exercise 1.27

from porty.report import read_portfolio


def portfolio_cost(filename):
    """Calculate total cost of stocks portfolio
    """
    total_purchase_cost = 0
    portfolio = read_portfolio(filename)

    # return sum([stock.cost for stock in portfolio])
    return portfolio.total_cost


def main(argv):
    if len(argv) == 2:
        f_path = argv[1]
    else:
        f_path = "Data/portfolio.csv"

    cost = portfolio_cost(f_path)
    print(f"Total purchase cost: {cost}")


if __name__ == "__main__":
    import sys
    main(sys.argv)
