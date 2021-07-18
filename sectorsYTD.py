import yfinance
import matplotlib.pyplot as plt

# ["GME", "AMC"],"Quetsch"
# ["LUS.DE"], "FTK.DE", "BWB.DE", "XTP.F"], "Neobroker"
# ["NEE", "IBE.MC", "AQN", "ORSTED.CO"], "Renewable Energy"

tickers = [["AAPL", "MSFT", "GOOG", "AMZN"], ["NEE", "ORSTED.CO", "AQN"],
           ["PLTR", "CRSR", "ARKK", "ARKG", "JKS"],
           ["PG", "JNJ", "WMT", "PEP", "KO", "CAT", "MMM", "JPM"],
           ["NVDA", "AMD", "QCOM"], ["MT", "GOLD", "CLF"]]
groupnames = ["Big Tech", "Renewable Energy", "Small Tech", "Value", "Chips", "Inflation"]

results = []


for group in tickers:
    groupresult = []

    closings = []
    dividends = []
    dates = []
    for ticker in group:
        stock = yfinance.Ticker(ticker)

        hist = stock.history(period="YTD")
        closings = hist["Close"].tolist()
        dividends = hist["Dividends"].tolist()

        if dates != [] and dates != list(hist.index.values):
            print("unterschiedliche datuemer!")
        dates = list(hist.index.values)

        i = 0
        for dividend in dividends:
            if dividend > 0:
                j = 0
                for closing in closings:
                    if j >= i:
                        closings[j] = closing + dividend
                    j = j + 1
            i = i + 1

        i = 0
        factor = closings[0]
        for closing in closings:
            closings[i] = (closings[i] / factor) / len(group)
            i = i + 1
        if groupresult == []:
            groupresult = closings
        else:
            for k in range(len(closings)):
                groupresult[k] = groupresult[k] + closings[k]
    results.append(groupresult)

i = 0
for group in groupnames:
    plt.plot(dates, results[i], label=group)
    i = i + 1
plt.legend()
plt.show()
