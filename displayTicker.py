##Retrieve a ticker symbol from mongodb and display the ticker symbol company name and price
from pymongo import MongoClient
import sys
import time
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
from config import mydb
matplotlib.use('TkAgg')


xpoints =[]
ypoints =[]
ticker = sys.argv[1]
tickerColl = mydb[ticker]##MongoDB

results = list(tickerColl.find())
for i,candle in enumerate(results):
    ypoints.append(candle['close'])
    try:
        xpoints.append(candle['datetime'].split(' ')[0])
    except:
        xpoints.append(candle['datetime'])

xpoints = np.array(xpoints)
ypoints = np.array(ypoints)

plt.xticks(np.arange(0, len(xpoints), 90))
plt.xticks(rotation=90)
plt.plot(xpoints, ypoints)
plt.title(ticker)
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()

