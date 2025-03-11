from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# Launch Chrome using ChromeDriver from PATH
driver = webdriver.Chrome()
driver.get("https://www.amazon.com")
time.sleep(10)
print("wait time for captcha solve")
links = driver.find_elements("xpath", "//a[@href]")

for link in links:
    print(link.get_attribute("innerHTML"))
time.sleep(15)
driver.quit() 