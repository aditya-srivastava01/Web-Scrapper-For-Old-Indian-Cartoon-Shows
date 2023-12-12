
import requests
import time
from bs4 import BeautifulSoup


url = f""
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser') 
down = soup.findAll(class_="dowloads")

