from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
# Авторизация
driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
# Покупки
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack"))
)
driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button#checkout"))
)
driver.find_element(By.CSS_SELECTOR, "button#checkout").click()
# Заполнение формы заказа
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input#first-name"))
)
driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys("Иван")
driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys("Петров")
driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "input#continue").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


def test_saucedemo():
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    print(total)
    assert total == "Total: $58.29"
