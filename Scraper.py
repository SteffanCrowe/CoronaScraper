import requests
import threading
from bs4 import BeautifulSoup
import ctypes
import time

class Scraper:
    def __init__(self):
        self.URL = 'https://www.worldometers.info/coronavirus/'

    def GetTable(self):
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find(id='main_table_countries')
        table_body = table.find('tbody')
        return table_body

    def GetNumInfectedFromTable(self, table):
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            countryName = cols[0].find(text=True)

            if countryName.startswith(' U.K.'):
                numInfected = cols[1].find(text=True)
                return numInfected
        return 0

    def GetNumInfected(self):
        table = self.GetTable()
        return self.GetNumInfectedFromTable(table)

def printNumInfected(scraper):
  threading.Timer(60.0, printNumInfected, [scraper]).start()
  global numInfected
  currentNumInfected = scraper.GetNumInfected()
  if numInfected != currentNumInfected:
    numInfected = currentNumInfected
    currentTime = time.gmtime()
    formattedTime = time.strftime("%c", currentTime)
    print("{} : {} Infected".format(formattedTime, numInfected))
    ctypes.windll.user32.MessageBoxW(0, "The current number of infected has increased to {}".format(numInfected), "U.K Corona", 0)

numInfected = 0
scraper = Scraper()
printNumInfected(scraper)
