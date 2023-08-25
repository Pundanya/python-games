import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Development/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://ru.wikipedia.org/wiki")

top_articles = driver.find_element(By.CSS_SELECTOR, ".main-top-articleCount b a")

all_portals = driver.find_element(By.LINK_TEXT, "Викисловарь")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

time.sleep(2)

# total_articles = int(''.join([x for x in top_articles.text if x.isdigit()]))
# print(total_articles)

