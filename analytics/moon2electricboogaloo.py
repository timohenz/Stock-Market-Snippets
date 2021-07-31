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
    lunationtoday = __get_lunation__(day)
    lunation3daysago = __get_lunation__(day - datetime.timedelta(days=3))
    # harvest moon plus a few following days
    if day.strftime("%m") == '08' and 0.45 < lunationtoday < 0.60:
        return "harvest moon"
    if 0.47 < lunation3daysago < 0.53:
        return "3 days after full moon"
    else:
        return "rest of the year"


stock = yfinance.Ticker("^GSPC")  # "^GSPC"#^DJI#SPY
hist = stock.history(period="max")  # 10Y
print(len(hist))

harvestmoons = [0]
threedaysafterfullmoon = [0]
restoftheyear = [0]

for i, row in hist.iterrows():
    dayopen = hist.loc[i, 'Close']
    nextdayopen = hist.shift(-1).loc[i, 'Close']
    change = 100 * ((nextdayopen - dayopen) / dayopen)
    phase = __get_phase__(i.to_pydatetime())

    if not numpy.isnan(change):
        if phase == "harvest moon":
            harvestmoons.append(change)
        if phase == "3 days after full moon":
            threedaysafterfullmoon.append(change)
        if phase == "rest of the year":
            restoftheyear.append(change)

fig, ax = plt.subplots()
phases = ['Harvest Moon', '3 Days after Full Moon', 'Rest of the Year']
ind = numpy.arange(3)

h = numpy.average(harvestmoons)
hm = h - numpy.std(harvestmoons)/9
hp = h + numpy.std(harvestmoons)/9
t = numpy.average(threedaysafterfullmoon)
tm = t - numpy.std(threedaysafterfullmoon)/9
tp = t + numpy.std(threedaysafterfullmoon)/9
r = numpy.average(restoftheyear)
rm = r - numpy.std(restoftheyear)/9
rp = r + numpy.std(restoftheyear)/9

stdm = [hm, tm, rm]
avg = [h, t, r]
stdp = [hp, tp, rp]

plt.bar(ind - 0.3, stdm, 0.2, color='lightblue')
plt.bar(ind, avg, 0.2, color='b')
plt.bar(ind + 0.3, stdp, 0.2, color='lightblue')

ax.set_xticks(ind)
ax.set_xticklabels(phases)
plt.title("Daily Stock Market Gains depending on Moon +- Standard deviation")
plt.savefig("moon2electricboogaloo.png")
