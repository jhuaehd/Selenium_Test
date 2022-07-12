from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time

# gets the chromedriver path
PATH = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

# directly go to the provided url
driver.get("https://techwithtim.net")

# gets the element name in the page and send following string to particular element name
# driver.find_element("name", "s").send_keys("python")
# driver.find_element(By.NAME, value="s").send_keys("python")
# driver.find_element(By.CSS_SELECTOR, value="type:submit").click()
driver.find_element(By.XPATH, value="//input[@type='search']").send_keys("python")
# driver.find_element(By.NAME, value="//input[@type='submit']").send_keys(Keys.ENTER)

# time.sleep(5)
# driver.close()


print("Test Completed Successfully")