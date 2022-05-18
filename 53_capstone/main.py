import time
from bs4 import BeautifulSoup
from selenium import webdriver
from keys import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

houses_links = []
houses_addresses = []
houses_prices = []

chrome_driver = "/home/sk/Project/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver))
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


zil_soup = BeautifulSoup(zil_html, "html.parser")

houses_urls = zil_soup.find_all("a", class_="list-card-link list-card-link-top-margin")
for x in houses_urls:
    houses_links.append(x["href"])

addresses = zil_soup.find_all("address", class_="list-card-addr")
for x in addresses:
    houses_addresses.append(x.getText())

price = zil_soup.find_all("div", class_="list-card-price")
for x in price:
    houses_prices.append(x.getText())


driver.get(gf_url)
for x in range(len(houses_addresses)):
    time.sleep(5)
    add_in = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_in.send_keys(f"{houses_addresses[x]}")
    price_in = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_in.send_keys(f"{houses_prices[x]}")
    link_in = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_in.send_keys(f"{houses_links[x]}")
    submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    another = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another.click()



driver.quit()

