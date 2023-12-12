
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import undetected_chromedriver as uc

url = f"https://185.53.88.15/category/bollywood-movies/bollywood-movies-2011-12/"
# option = webdriver.ChromeOptions()
# option.add_argument('headless')
driver = webdriver.Chrome('chromedriver')
driver.get(url)
r = driver.find_elements(By.CLASS_NAME,"ml-mask jt")
for i in r:
    print(i.text)
driver.close()



