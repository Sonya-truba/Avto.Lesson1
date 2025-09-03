from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class InputData:

    def __init__(self, driver):
        """
                Конструктор класса CalcMainPage.
                :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step("Установка задержки {time} секунд.")
    def delay(self, time):
        """
                Устанавливает задержку для выполнения операций на калькуляторе.
                :param time: int — время задержки в секундах.
        """
        self._driver.find_element(By.ID, "delay").clear()
        self._driver.find_element(By.ID, "delay").send_keys(time)

    @allure.step("Нажатие кнопки '{button}'.")
    def press_calculation_button(self, button):
        """
                Уменьшает разрешение экрана.
                Дожидается кликабельности кнопки "="
                Нажимает на кнопку калькулятора.
                :param button: str — текст на кнопке, которую нужно нажать.
        """
        self._driver.execute_script("document.body.style.zoom='25%'")
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']")))
        self._driver.find_element(By.XPATH, button).click()
