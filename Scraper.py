import requests
from bs4 import BeautifulSoup

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

scraper = Scraper()
print(scraper.GetNumInfected())