# CoronaScraper
 Scrape the current number of infected in the UK

## Installation
### Setup python environment and install libraries
1) cd to the top level directory
2) python -m venv ./env
3) run activate.bat under env\Scripts
4) pip install -r requirements.txt

## Run
After installation just run Startup.bat  
Every 60 seconds it will check https://www.worldometers.info/coronavirus/  
If there is a difference in the UK number it will notify you and log to the console  
It only runs while the console is open  