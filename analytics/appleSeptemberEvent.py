import datetime

import numpy
import yfinance
import matplotlib.pyplot as plt

prices2020 = []
prices2019 = []
prices2018 = []
prices2017 = []
prices2016 = []
prices2015 = []

event2020 = numpy.datetime64('2020-09-15')
event2019 = numpy.datetime64('2019-09-10')
event2018 = numpy.datetime64('2018-09-12')
event2017 = numpy.datetime64('2017-09-12')
event2016 = numpy.datetime64('2016-09-07')
event2015 = numpy.datetime64('2015-09-09')

stock = yfinance.Ticker('AAPL')
hist = stock.history(period="max")
closings = hist["Close"].tolist()
dates = list(hist.index.values)

for i in range(len(dates)-7):
    # days before event does not wort - it screws the data depending on weekends
    #if (event2020 + numpy.timedelta64(7, 'D')) > dates[i] > (event2020 - numpy.timedelta64(14, 'D')):
    if dates[i-7] < event2020 < dates[i+7]:
        prices2020.append(closings[i])
    if dates[i-7] < event2019 < dates[i+7]:
        prices2019.append(closings[i])
    if dates[i-7] < event2018 < dates[i+7]:
        prices2018.append(closings[i])
    if dates[i-7] < event2017 < dates[i+7]:
        prices2017.append(closings[i])
    if dates[i-7] < event2016 < dates[i+7]:
        prices2016.append(closings[i])
    if dates[i-7] < event2015 < dates[i+7]:
        prices2015.append(closings[i])

i = 0
factor = prices2020[6]
for price in prices2020:
    prices2020[i] = (prices2020[i] / factor)
    i = i + 1
i = 0
factor = prices2019[6]
for price in prices2019:
    prices2019[i] = (prices2019[i] / factor)
    i = i + 1
i = 0
factor = prices2018[6]
for price in prices2018:
    prices2018[i] = (prices2018[i] / factor)
    i = i + 1
i = 0
factor = prices2017[6]
for price in prices2017:
    prices2017[i] = (prices2017[i] / factor)
    i = i + 1
i = 0
factor = prices2016[6]
for price in prices2016:
    prices2016[i] = (prices2016[i] / factor)
    i = i + 1
i = 0
factor = prices2015[6]
for price in prices2015:
    prices2015[i] = (prices2015[i] / factor)
    i = i + 1

daysfromevent = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]

plt.title("Apple Stock before and after September Event")
plt.plot(daysfromevent, prices2020, label='2020')
plt.plot(daysfromevent, prices2019, label='2019')
plt.plot(daysfromevent, prices2018, label='2018')
plt.plot(daysfromevent, prices2017, label='2017')
plt.plot(daysfromevent, prices2016, label='2016')
plt.plot(daysfromevent, prices2015, label='2015')
plt.xlabel("Days before/after")
plt.axvline(x=0, color='black', linestyle='--')
plt.legend()
plt.show()
