# Stock-Market-Snippets

A collection of my small scripts (or code snippets only) used to analyze the stock market.

## Usage

Many of these Scripts could be used to feed Data into Boosting/Bagging algorithms for algo trading.

## Overview

### sectorsYTD

Small script that shows which sectors/groups of stocks performed YTD. 
The stocks in every manual bucket is equal weighted (not market cap.).
Returns Line chart. 1 = start value = 100% of original investment. 
0.8 = 80% of original investment = -20% YTD. etc.

### earningsNotification

A script that notifies me when one of my holdings has an earnings call in the upcoming week.
It uses a telegram bot and runs on a Raspberry Pi.
Schedule it to run on mondays 3:00AM via python scheduler or bash/batch.
Adjust tickers at very bottom.

### moonStocksCorrelation

Some lunatic (pun intended) on a forum claimed there was a correlation between the stock market and moon phases. Of course it is not true.
The moon is way to predictable and obvious for a self-fullfilling prophecy. It gets arbitraged away. You can try out different indices or timeframes.
