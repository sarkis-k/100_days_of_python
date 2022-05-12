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

# My solution hard-coded
event_dict = {}
for x in range(1,6):
    date_items = driver.find_element(by=By.XPATH, value=f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{x}]/time')
    event_items = driver.find_element(by=By.XPATH, value=f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{x}]/a')
    event_dict[x-1] = {
        "time": date_items.get_attribute("datetime").split("T")[0],
        "name": event_items.text
    }

print(event_dict)

# Her solution a bit better
event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for x in range(0,len(event_times)):
    events[x]={
        "time": event_times[x].text,
        "name": event_names[x].text
    }
print(events)

driver.quit()

