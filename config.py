import pymongo
from tda.auth import easy_client
from tda.client import Client
from tda.streaming import StreamClient
import os

CONSUMER_KEY = ''
client_pass = ''
TD_ACCOUNT = ''
JSON_PATH ='./json_state.json'
REDIRECT_URI = 'https://127.0.0.1/test'

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["tda"]
TDclient = easy_client(
        api_key=CONSUMER_KEY,
        redirect_uri=REDIRECT_URI,
        token_path=JSON_PATH)

# get stock from getSP500.txt 
if(os.path.exists('sp500_stocks.txt')):
    with open('sp500_stocks.txt','r') as f:
        sp500_stocks = eval(f.read())
else:
    print("sp500_stocks.txt not found. Run getSP500.py first")
    exit()
