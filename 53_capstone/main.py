import time
from pprint import pprint

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from keys import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


houses_links = []
houses_addresses = []
houses_prices = []


chrome_driver = "/home/sk/Project/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver))
# driver.set_window_position(0, 0)
# driver.set_window_size(2048, 1536)
driver.get(zil_url)
time.sleep(2)
html = driver.find_element(by=By.TAG_NAME, value='html')
html.send_keys(Keys.PAGE_DOWN)
html.send_keys(Keys.PAGE_DOWN)
html.send_keys(Keys.PAGE_DOWN)
html.send_keys(Keys.PAGE_DOWN)
html.send_keys(Keys.PAGE_DOWN)
html.send_keys(Keys.PAGE_DOWN)
zil_html = driver.page_source





# header ={ "Accept-Language": "en-US,en;q=0.9,ar;q=0.8,ms;q=0.7",
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
# }
# website = requests.get(zil_url, headers=header)
# zil_web = website.text
zil_soup = BeautifulSoup(zil_html, "html.parser")

ul = zil_soup.find("ul", class_="photo-cards photo-cards_wow photo-cards_short photo-cards_extra-attribution")

houses_urls = zil_soup.find_all("a", class_="list-card-link list-card-link-top-margin")
for x in houses_urls:
    # print(x["href"])
    houses_links.append(x["href"])
addresses = zil_soup.find_all("address", class_="list-card-addr")
for x in addresses:
    print(x.getText())
    houses_addresses.append(x.getText())

price = zil_soup.find_all("div", class_="list-card-price")
for x in price:
    print(x.getText())
    houses_prices.append(x.getText())


driver.get(gf_url)
time.sleep(5)



driver.quit()

