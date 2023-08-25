from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:/Development/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR, ".shrubbery time")
event_articles = driver.find_elements(By.CSS_SELECTOR, ".shrubbery li a")
upcoming_events = {}

for i in range(len(event_dates)):
    date = event_dates[i].get_attribute("datetime").split("T")[0]
    article = event_articles[i].text
    upcoming_events[i] = {
        "time": date,
        "name": article
    }

print(upcoming_events)
