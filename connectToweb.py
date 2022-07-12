from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time

# gets the chromedriver path
PATH = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

# directly go to the provided url
driver.get("https://login.yahoo.com/?.intl=us")

# gets the element name in the page and send following string to particular element name
# driver.find_element("name", "s").send_keys("python")
# driver.find_element(By.NAME, value="s").send_keys("python")
# driver.find_element(By.CSS_SELECTOR, value="type:submit").click()
driver.find_element(By.ID, value="login-username").send_keys("abcd@yahoo.com")
driver.find_element(By.XPATH, value="//input[@value='Next']").click()


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# driver.find_element(By.XPATH, value="//input[@type='search']").send_keys("python")
# driver.find_element(By.NAME, value="//input[@type='submit']").send_keys(Keys.ENTER)


print("Test Completed Successfully")