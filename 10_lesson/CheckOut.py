from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckOut:

    def __init__(self, driver):
        """
        Конструктор класса CheckOut.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Переход к оформлению заказа.")
    def click_check_out_button(self):
        """
        Нажатие кнопки 'Заказа'.
        :return: str
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button#checkout"))
        )
        self._driver.find_element(By.CSS_SELECTOR, "button#checkout").click()
