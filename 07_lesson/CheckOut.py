from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckOut:

    def __init__(self, driver):
        self._driver = driver

    def check_out(self, driver):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button#checkout"))
        )
        self._driver.find_element(By.CSS_SELECTOR, "button#checkout").click()
