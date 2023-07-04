# StockTracker
 A stock tracker which leverages Python with SciKit Learn, MongoDB and TD Ameritrade APIs. Creates a real time viewable stream and stores the daily data into MongoDB. This follows with clustering algorithms to see correlated data and work towards a trading bot, but for now make better investment decisions of our own


pip3.7 install -r requirements.txt

1st Time - python getSP500.py

python main.py

python displayTicker.py TCKR


NOTE!
config.py requires TD API credentials which are getting sunsetted. Only a prior existing developer account can utilize this code until the Charles-Schwab merge.

./streamingClient allows for a "real time" (1 candle per minute) data stream. Does not currently account for market hours.