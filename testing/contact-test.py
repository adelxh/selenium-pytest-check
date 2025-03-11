from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.marchofdimes.ca/en-ca")
time.sleep(3)
# looking for about us button 
about_us_button = driver.find_element(By.PARTIAL_LINK_TEXT, "About Us").click()
driver.execute_script("window.scrollTo(0,800);")
time.sleep(3)
contact_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Contact Us").click()
first_name = driver.find_element(By.ID, "ctl00_ctl45_g_8f8b241c_7957_40e2_8b49_ea9fdf5d5ad1_FullName").send_keys("john")
email_address = driver.find_element(By.ID, "ctl00_ctl45_g_8f8b241c_7957_40e2_8b49_ea9fdf5d5ad1_EmailAddress").send_keys("ddd@gmail.com")
send_button = driver.find_element(By.ID, "ctl00_ctl45_g_8f8b241c_7957_40e2_8b49_ea9fdf5d5ad1_submit").click()
with open ("test-auth.txt", "a") as log:
    log.write(f"User filled out partially and form shouldnt submit - FAILED\n")
time.sleep(10)

driver.quit(); 