import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:/Development/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get("https://orteil.dashnet.org/cookieclicker/")


try:
    lang = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
except:
    print("Язык выбран")
    pass
else:
    lang.click()

time.sleep(2)
cookie = driver.find_element(By.ID, "bigCookie")

five_s = time.time() + 5
five_m = time.time() + 60*5

while True:
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()

    if time.time() > five_s:
        while True:
            try:
                upgrade = driver.find_element(By.XPATH, '//*[@class="crate upgrade enabled"]')
            except NoSuchElementException:
                break
            else:
                upgrade.click()
                break

        while True:
            products = driver.find_elements(By.XPATH, '//*[@class="product unlocked enabled"]')
            if products:
                products[-1].click()
            else:
                break

        five_s = time.time() + 5

    if time.time() > five_m:
        print("Your score after 5 min:", driver.find_element(By.ID, "cookiesPerSecond").text)
        break

driver.quit()
