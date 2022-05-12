from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver = "/home/sk/Project/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver))

driver.get("https://www.python.org")

# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# doc_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

# bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)




driver.quit()