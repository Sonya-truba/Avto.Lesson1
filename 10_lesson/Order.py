from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Order:

    def __init__(self, driver):
        """
        Конструктор класса Order.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Заполнение формы личными данными для заказа.")
    def fill_order_form(self, name, family, code):
        """
        Заполняет форму личными данными.
        :param name: str — текст, который вводится в поле.
        :param family: str — текст, который вводится в поле.
        :param code: str — текст, который вводится в поле.
        :return: str
        """
        WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input#first-name"))
        )
        self._driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys(family)
        self._driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys(code)
        self._driver.find_element(By.CSS_SELECTOR, "input#continue").click()

    @allure.step("Вывод итоговой стоимости.")
    def summary_total(self):
        """
        Выводит значение итоговой стоимости.
        :return: str
        """
        total_price = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total_price
