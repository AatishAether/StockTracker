from tda import auth
import time
import pandas as pd

from datetime import datetime
from config import *

token_path = JSON_PATH
api_key = CONSUMER_KEY+'@AMER.OAUTHAP'
redirect_uri = REDIRECT_URI

stockUniverse = sp500_stocks

def fixDateTime(candle):
    return datetime.fromtimestamp(candle['datetime']/1000.0).strftime('%Y-%m-%d %H:%M:%S')
##LOGIN & AUTH
try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome() as driver:
        c = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)

for stock in stockUniverse:
    #If stock name exists in database, skip
    if(stock in mydb.list_collection_names()):
        print("Skipping: "+stock)
        continue
    else:
        r = c.get_price_history_every_day(stock)
        assert r.status_code == 200, r.raise_for_status()
        candles = r.json()['candles']
        ##Insert data into mongodb
        TICKER = mydb[stock]
        for candle in candles:
           candle['datetime'] = fixDateTime(candle)
           ##Check for duplicates
           TICKER.insert_one(candle)


#r = c.get_price_history_every_day('META')
#assert r.status_code == 200, r.raise_for_status()
##extract candles from json response
#candles = r.json()['candles']
##Store candles into mongodb
#TICKER = mydb['META']
#for candle in candles:
#    candle['datetime'] = fixDateTime(candle)
#    ##Check for duplicates
#    if(TICKER.find_one({'datetime':candle['datetime']})):
#        continue
#    else:
#        TICKER.insert_one(candle)

