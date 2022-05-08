import numpy
import yfinance

ticker = 'SPOT'
quaterly = True


def main():
    stock = yfinance.Ticker(ticker)  # SPOT
    if quaterly:
        df = stock.quarterly_financials
    else:
        df = stock.financials
    date = df.axes[1][0]
    axes = df.axes[0].tolist()

    revenue = df[date].loc['Total Revenue']
    cost_of_revenue = df[date].loc['Cost Of Revenue']
    gross_profit = df[date].loc['Gross Profit']
    operating_income = df[date].loc['Operating Income']
    opex = df[date].loc['Total Operating Expenses'] - cost_of_revenue
    rnd = df[date].loc['Research Development']
    sga = df[date].loc['Selling General Administrative']
    other_opex = df[date].loc['Other Operating Expenses']

    # net_income = df[date].loc['Net Income']
    # interest = df[date].loc['Interest Expense']
    # tax = df[date].loc['Income Tax Expense']
    # # TODO Interest and Tax

    print("Revenue [" + str(revenue) + "] Total Revenue")
    print("Total Revenue [" + str(cost_of_revenue) + "] Cost Of Revenue")
    print("Total Revenue [" + str(gross_profit) + "] Gross Profit")
    if operating_income < 0:
        print("Unprofitability [" + str(abs(operating_income)) + "] Gross Profit")
    else:
        print("Gross Profit [" + str(operating_income) + "] Operating Profit")
    print("Gross Profit [" + str(opex) + "] Opex")
    print("Opex [" + str(sga) + "] SG&A")
    print("Opex [" + str(other_opex) + "] Other Opex")
    print("Opex [" + str(rnd) + "] RnD")

    # if tax > 0:
    #     print("Operating Profit [" + str(tax) + "] Tax")
    # else:
    #     print("Tax [" + str(-tax) + "] Net Income")
    #     net_income += tax
    # if interest < 0:
    #     print("Interest [" + str(-interest) + "] Net Income")
    #     net_income += interest
    # else:
    #     print("Operating Profit  [" + str(interest) + "] Interest")
    # print("Operating Profit [" + str(net_income) + "] Net Income")

    print("//go to sankeymatic.com")


if __name__ == "__main__":
    main()
