import datetime
from config import *


today = datetime.datetime.today()
EQUITY = TDclient.Markets('EQUITY')

hours = TDclient.get_hours_for_multiple_markets(EQUITY,today)
isOpen = hours.json()['equity']['EQ']['isOpen']
if(not isOpen):
   print("Market is closed! Try again when the market is open")
   exit()