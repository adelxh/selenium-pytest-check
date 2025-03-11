import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

@pytest.fixture
def driver(): 
    options = Options()
    options.add_argument("--enable-javascript")
    options.add_experimental_option("excludeSwitches", ["disable-popup-blocking", "enable-automation"])

    driver = webdriver.Chrome(options=options) 
    yield driver
    driver.quit()

def test_site_open(driver): 
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

def test_dropdown_options(driver): 
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    select_options = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(select_options)
    options = [option.text for option in select.options]
    num_options = len(options) # total number of options 

    # loops through all options and clicks on each one of them, 5 second wait time before other option is clicked 

    for i in range(num_options):
        select_options = driver.find_element(By.CLASS_NAME, "product_sort_container")
        select = Select(select_options)

        option_text = options[i]
        select.select_by_visible_text(option_text) 
        with open("script.txt", "w") as file: 
            file.write(f"T0001: Dropdown options - PASSED\n")
            
            time.sleep(5)

def test_title_ascending(driver): 
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    select_options = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(select_options)
    select.select_by_visible_text("Name (A to Z)") 

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))

    )
    
    item_title = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    with open("script.txt", "a") as file:
        text = [titles.text.strip() for titles in item_title]

        if text == sorted(text):
            file.write(f"T0005 - Title in Ascending order - PASSED\n")
        else:
            file.write(f"T0005 - Title in Ascending order - FAILED\n")

def test_title_descending(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    select_options = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(select_options)
    select.select_by_visible_text("Name (Z to A)") 

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))

    )
    
    item_title = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    with open("script.txt", "a") as file:
        text = [titles.text.strip() for titles in item_title]

        if text == sorted(text, reverse=True):
            file.write(f"T0005 - Title in Descending order - PASSED\n")
        else:
            file.write(f"T0005 - Title in Descending order - FAILED\n")

             



        
def test_price_L_H(driver): 
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    select_options = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(select_options)
    select.select_by_visible_text("Price (low to high)") 

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price"))
    )
   
    price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    if not price:
         print("No price elements found")
         return

    with open("script.txt", "w") as file: 

         price_convert = [float(el.text.replace("$", "").replace(",","").strip()) for el in price]
         try:
             
            sorted_price = sorted(price_convert)
            file.write(f"{sorted_price}\n")

            assert price_convert == sorted(price_convert), "T0002: Price from Low to High - FAILED"

            file.write("T0002: Price from Low to High - PASSED\n")
         except ValueError as e: 
             print(f"error {e}")


def test_price_H_L(driver): 
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    select_options = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(select_options)
    select.select_by_visible_text("Price (high to low)") 

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price"))
    )
    time.sleep(5)
    price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    if not price:
         print("No price elements found")
         return
    with open("script.txt", "w") as file: 

         price_convert = [float(el.text.replace("$", "").replace(",","").strip()) for el in price]
         try:
             
            sorted_price = sorted(price_convert, reverse=True)
            file.write(f"{sorted_price}\n")

            assert price_convert == sorted(price_convert, reverse=True), "T0003: Price from Hight to Low - FAILED"

            file.write("T0003: Price from High to Low - PASSED\n")
         except ValueError as e: 
             print(f"error {e}")



        
    
    


        


   
       
    

    
    

