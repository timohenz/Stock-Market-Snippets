import datetime
import random
import time
import pandas
import yfinance
import os


def __send_message__(apikey, chatid, message):
    os.system('curl -k https://api.telegram.org/bot' + str(apikey) + '/sendMessage ' +
              '-d chat_id='+str(chatid)+' -d text="' + message + '"')


def __calendar__(ticker, api_key, chatid):
    stock = yfinance.Ticker(ticker)
    if (stock.calendar is not None):
        events = (stock.calendar.iloc[0].to_numpy())
        print(stock.calendar)
        for e in events:
            d1 = datetime.datetime.now()
            d2 = datetime.datetime.now() + datetime.timedelta(days=7)
            if d1 < e < d2:
                __send_message__(api_key, chatid, 'Am ' + __weekday__(e.weekday()) +
                                 ' Earnings von ' + stock.info['longName'] +
                                 '. https://seekingalpha.com/symbol/' + ticker +
                                 '/earnings')


def __weekday__(num):
    if (num == 0):
        return 'Montag'
    if (num == 1):
        return 'Dienstag'
    if (num == 2):
        return 'Mittwoch'
    if (num == 3):
        return 'Donnerstag'
    if (num == 4):
        return 'Freitag'
    if (num == 5):
        return 'Samstag'
    else:
        return 'Sonntag'


def run(api_key, chatid):
    tickers = ['AAPL', 'PEP']
    for ticker in tickers:
        __calendar__(ticker, api_key, chatid)
