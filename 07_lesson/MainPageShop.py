from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self._driver = driver

    def shopping(self, driver, product):
        self._driver.execute_script("document.body.style.zoom='25%'")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, product))
        )
        self._driver.find_element(By.CSS_SELECTOR, product).click()

    def buy(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
