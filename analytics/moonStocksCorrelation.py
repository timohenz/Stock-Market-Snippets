import datetime
import ephem
import yfinance
import numpy
import matplotlib.pyplot as plt


# lunation of moon from 0 to 1
# 1/0 is new moon. 0.5 is full moon
def __get_lunation__(day):
    date = ephem.Date(day)
    nnm = ephem.next_new_moon(date)
    pnm = ephem.previous_new_moon(date)
    lunation = (date - pnm) / (nnm - pnm)
    return lunation


# phase of the moon: ascending, full moon, descending, new moon
# only works more or less. Sometimes you have to +/- a day
def __get_phase__(day):
    tomorrow = day + datetime.timedelta(days=1)
    lunationtoday = __get_lunation__(day)
    if lunationtoday > 0.97 or lunationtoday < 0.03:
        return "new moon"
    if 0.47 < lunationtoday < 0.53:
        return "full moon"
    if lunationtoday < 0.47:
        return "ascendant"
    if lunationtoday > 0.53:
        return "descendant"
    else:
        return "error"


def main():
    stock = yfinance.Ticker("^GSPC")  # "^GSPC"#^DJI#SPY
    hist = stock.history(period="max")  # 10Y
    print(len(hist))

    # sum of percent change
    sumfullmoon = 0
    sumnewmoon = 0
    sumascend = 0
    sumdescend = 0
    # counters
    numfullmoon = 0
    numnewmoon = 0
    numascend = 0
    numdescend = 0

    for i, row in hist.iterrows():
        dayopen = hist.loc[i, 'Close']
        nextdayopen = hist.shift(-1).loc[i, 'Close']
        change = 100 * ((nextdayopen - dayopen) / dayopen)
        phase = __get_phase__(i.to_pydatetime())

        if not numpy.isnan(change):
            if phase == "new moon":
                sumnewmoon += change
                numnewmoon += 1
            if phase == "full moon":
                sumfullmoon += change
                numfullmoon += 1
            if phase == "ascendant":
                sumascend += change
                numascend += 1
            if phase == "descendant":
                sumdescend += change
                numdescend += 1

    fig, ax = plt.subplots()
    phases = ['New Moon', 'Full Moon', 'Ascendant', 'Descendant']
    avg = [sumnewmoon / numnewmoon, sumfullmoon / numfullmoon, sumascend / numascend, sumdescend / numdescend]
    ax.bar(phases, avg)
    ind = numpy.arange(4)
    ax.set_xticks(ind)
    ax.set_xticklabels(phases)
    plt.title("Average Daily Stock Market Gains per Moon Phase")
    plt.savefig("moonStocksCorrelation.png")


if __name__ == "__main__":
    main()
