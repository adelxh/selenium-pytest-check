import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture 
def driver(): 
    driver = webdriver.Chrome()
    yield driver 
    driver.quit() 

def test_open_login(driver): 
    driver.get("https://www.saucedemo.com")
    assert "Swag Labs" in driver.title, "Title Mismatch"
    with open("test-cases.txt", "a") as log: 
        log.write(f"Login page opened - PASSED \n")

def test_login_success(driver): 
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url, "Login failed"

    with open("test-cases.txt", "a") as log: 
        log.write(f"User log in to site - PASSED \n")

def test_add_to_cart(driver): 
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
    driver.find_element(By.ID, "add-to-cart").click()
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert "1" in cart.text, "Item not added"

    with open("test-cases.txt", "a") as log: 
        log.write(f"User adds item to cart - PASSED \n")

def test_checkout(driver): 
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() 
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("abscd")
    driver.find_element(By.ID, "last-name").send_keys("abscd")
    driver.find_element(By.ID, "postal-code").send_keys("abc3pfv")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    assert "checkout-complete" in driver.current_url, "Checkout didnt complete"
    with open("test-cases.txt", "a") as log: 
        log.write(f"User completes checkout - PASSED\n")




    
