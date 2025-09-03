from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:

    def __init__(self, driver):
        """
        Конструктор класса MainPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    @allure.step("Выбор позиций товаров.")
    def shopping(self, product):
        """
        Уменьшает разрешение экрана.
        Наполняет корзину позициями товаров.
        :param product: str - позиции товаров с соответствующим названием кнопок с использованием CSS-selector.
        :return: str
        """
        self._driver.execute_script("document.body.style.zoom='25%'")
        WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, product))
        )
        self._driver.find_element(By.CSS_SELECTOR, product).click()

    @allure.step("Переход в корзину.")
    def click_buy_button(self):
        """
        Нажатие кнопки 'Корзина'.
        :return: str
        """
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
