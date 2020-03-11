import requests
import threading
from bs4 import BeautifulSoup
import ctypes
import time

class Scraper:
    def __init__(self):
        self.URL = 'https://www.worldometers.info/coronavirus/'

    def GetTable(self):
        try:
            page = requests.get(self.URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            table = soup.find(id="main_table_countries")
            table_body = None
            if table is not None:
                table_body = table.find('tbody')
            return table_body
        except:
            return None # Problems requesting the page? just return none

    def GetNumInfectedFromTable(self, table):
        if table is not None:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                countryNameColumn = cols[0]
                countryNameHyper = countryNameColumn.find('a')
                if countryNameHyper is not None:
                    countryName = countryNameHyper.find(text=True)
                    if countryName.startswith('UK'):
                        numInfected = cols[1].find(text=True)
                        return numInfected
        return None

    def GetNumInfected(self):
        table = self.GetTable()
        return self.GetNumInfectedFromTable(table)

def printNumInfected(scraper):
    threading.Timer(60.0, printNumInfected, [scraper]).start()
    global numInfected
    currentNumInfected = scraper.GetNumInfected()
    if currentNumInfected is not None:
        if numInfected != currentNumInfected:
            numInfected = currentNumInfected
            currentTime = time.gmtime()
            formattedTime = time.strftime("%c", currentTime)
            print("{} : {} Infected".format(formattedTime, numInfected))
            ctypes.windll.user32.MessageBoxW(0, "The current number of infected has increased to {}".format(numInfected), "U.K Corona", 0)
    else:
        print("Error getting table from " + scraper.URL)

numInfected = 0
scraper = Scraper()
printNumInfected(scraper)
