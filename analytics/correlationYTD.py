import numpy
from scipy.stats import pearsonr
import yfinance
import matplotlib.pyplot as plt

tickers = [["SPY"],
           ["AAPL", "MSFT", "GOOG", "AMZN"],
           ["MT", "CLF"],
           ["PG", "JNJ", "WMT", "PEP", "KO", "CAT", "MMM", "JPM"],
           ["NVDA", "AMD", "QCOM"],
           ["BND", "18MW.DE", "HYG"],
           ["GLD"],
           ["IWM", "IWM", "ARKK", "ARKG"]]
groupnames = ["SPY", "Big Tech", "Stahlthese", "Value", "Chips", "Bonds", "Gold", "Growth\nNebenwerte"]

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

        # adjust for dividend
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
            # everyone starts form 0 for equal weight - also number of securities in basket
            closings[i] = (closings[i] / factor) / len(group)
            i = i + 1
        if not groupresult:
            groupresult = closings
        else:
            for k in range(len(closings)):
                groupresult[k] = groupresult[k] + closings[k]
    results.append(groupresult)

# prepare data for bar chart
data = []
for r in results:
    corr, _ = pearsonr(results[0], r)  # numpy.correlate(results[0], r)[0] corrcoef
    data.append(corr)

# matplotlib bar chart
fig, ax = plt.subplots()
ind = numpy.arange(len(groupnames))
plt.bar(ind, data, label=groupnames)
ax.set_xticks(ind)
ax.set_xticklabels(groupnames, rotation=30)
plt.title("Correlation with S&P500")
plt.savefig("correlation.png", bbox_inches="tight")
