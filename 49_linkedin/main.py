import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from keys import *
import re

chrome_driver = "/home/sk/Project/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver))
driver.set_window_position(0, 0)
driver.set_window_size(2048, 1536)
linkedin = "https://www.linkedin.com/jobs/search/?distance=25.0&f_AL=true&f_WT=1%2C2%2C3&geoId=103644278&keywords=python%20developer&sortBy=R"


driver.get(linkedin)

signin = driver.find_element(by=By.CLASS_NAME, value="nav__button-secondary")
signin.click()
time.sleep(2)
email_input = driver.find_element(by=By.ID, value="username")
email_input.send_keys(username)
pass_input = driver.find_element(by=By.ID, value="password")
pass_input.send_keys(pswd)
pass_input.send_keys(Keys.ENTER)
time.sleep(2)

easy_apply = driver.find_elements(by=By.XPATH, value='/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div/div/button')
easy_apply.click()

next_but = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button')
next_but.click()

review_b = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/form/footer/div[2]/button[2]')
review_b.click()

submit_b = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/footer/div[3]/button[2]')
submit_b.click()




# Not finished all jobs apply
# all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
#
# for listing in all_listings:
#     print("called")
#     listing.click()
#     time.sleep(2)
#
#     try:
#         easy_apply = driver.find_element(by=By.CLASS_NAME, value=".jobs-s-apply button")
#         easy_apply.click()
#
#         next_but = driver.find_element(by=By.CLASS_NAME, value="")
#         next_but.click()
#
#         review_b = driver.find_element(by=By.XPATH, value='')
#         review_b.click()
#
#         submit_b = driver.find_element(by=By.XPATH, value='')
#         submit_b.click()
#
#         close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
#         close_button.click()
#
#     except NoSuchElementException:
#         print("No application button, skipped.")
#         continue
#
#
