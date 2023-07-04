from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time


url = "https://www.slickcharts.com/sp500"
driver = webdriver.Chrome()  # You can use any webdriver you prefer

driver.get(url)
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'class': 'table table-hover table-borderless table-sm'})

sp500_stocks = []
for row in table.tbody.find_all('tr'):
    ticker = row.find_all('td')[2].text.strip()
    sp500_stocks.append(ticker)

#write stocks to file
with open('sp500_stocks.txt','w') as f:
    f.write(str(sp500_stocks))