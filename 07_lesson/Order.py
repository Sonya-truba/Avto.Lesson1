from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Order:

    def __init__(self, driver):
        self._driver = driver

    def order(self, driver, name, family, code):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input#first-name"))
        )
        self._driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys(family)
        self._driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys(code)
        self._driver.find_element(By.CSS_SELECTOR, "input#continue").click()

    def total(self):
        total_price = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total_price
