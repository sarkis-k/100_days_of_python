from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver = "/home/sk/Project/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver))

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # number = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# # number.click()
#
# all_portals = driver.find_element(by=By.LINK_TEXT, value="Content portals")
# # all_portals.click()
#
# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
name = driver.find_element(by=By.NAME, value="fName")
name.send_keys("john")
l_name = driver.find_element(by=By.NAME, value="lName")
l_name.send_keys("smith")
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("jsmith@ohn.com")
email.send_keys(Keys.ENTER)

