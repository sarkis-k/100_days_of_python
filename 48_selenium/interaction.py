from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver = "/home/sk/Project/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# number.click()


all_portals = driver.find_element(by=By.LINK_TEXT, value="Content portals")
all_portals.click()