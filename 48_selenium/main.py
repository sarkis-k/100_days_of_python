from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



chrome_driver = "/home/sk/Project/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver))

driver.get("https://www.python.org")
search_bar = driver.find_element(by=By.NAME, value="q")

print(search_bar.get_attribute("placeholder"))


driver.quit()