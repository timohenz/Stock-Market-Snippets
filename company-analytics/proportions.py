import numpy
import yfinance
import matplotlib.pyplot as plt

# ToDo try out Seaborn

ticker = 'VWAGY'


def main():
    stock = yfinance.Ticker(ticker)
    financials = stock.financials
    balance_sheet = stock.balance_sheet

    date = financials.axes[1][0]

    revenue = financials[date].loc['Total Revenue']
    operating_income = financials[date].loc['Operating Income']
    total_liabilities = balance_sheet[date].loc['Total Liab']
    total_assets = balance_sheet[date].loc['Total Assets']
    market_cap = stock.info['marketCap']

    fig, ax = plt.subplots()
    labels = ['Market Cap.', 'Annual \n Revenue', 'Annual \n Operating \n Income', 'Liabilities', 'Assets']
    y = [market_cap, revenue, operating_income, total_liabilities, total_assets]
    ax.bar(labels, y)
    ind = numpy.arange(5)
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    plt.title("Proportions of Company")
    plt.savefig("proportions.png")


if __name__ == "__main__":
    main()
