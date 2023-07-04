import asyncio
import json
from datetime import datetime

from config import TDclient, TD_ACCOUNT, sp500_stocks
from marketHours import * 
stockUniverse = sp500_stocks[0:4]


stream_client = StreamClient(TDclient, account_id=TD_ACCOUNT)
myDB = myClient['TDAstream']##Switch DB from default config of tda
async def read_stream():
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.EXPRESS)

    def receive_message(message):
        print(json.dumps(message,indent=2))
        for item in message['content']:
            data = {}
            data['open'] = item['OPEN_PRICE']
            data['high'] = item['HIGH_PRICE']
            data['low'] = item['LOW_PRICE']
            data['close'] = item['CLOSE_PRICE']
            data['volume'] = item['VOLUME']
            data['datetime'] = item['CHART_TIME']
            #convert datetime to epoch
            newDateTime = datetime.datetime.fromtimestamp(data['datetime']/1000.0)
            data['datetime'] = newDateTime.strftime('%Y-%m-%d %H:%M:%S')
            #newDateTime = datetime.datetime.strptime(str(data['datetime']),'%Y-%m-%dT%H:%M:%S+0000')
            #print(data['datetime'])
            

            ticker = item['key']
            mydb[ticker].insert_one(data)

            
        with open("candle.txt",'a') as f:
            f.write(str(data)+'\n')

        print("inserted candle")


    # Always add handlers before subscribing because many streams start sending
    # data immediately after success, and messages with no handlers are dropped.
    #stream_client.add_nasdaq_book_handler(print_message)
    #await stream_client.nasdaq_book_subs(stockUniverse[0])
    stream_client.add_chart_equity_handler(receive_message)
    await stream_client.chart_equity_subs(stockUniverse)

    while True:
        await stream_client.handle_message()

asyncio.run(read_stream())