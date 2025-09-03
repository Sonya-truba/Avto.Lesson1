from selenium.webdriver.common.by import By
import allure


class Auth:

    def __init__(self, driver):
        """
        Конструктор класса Auth.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step("Заполнение формы авторизации.")
    def login_with_credentials(self, login, password):
        """
        Заполняет форму авторизации с использованием логина и пароля .
        :param login: str — текст, который вводится в поле.
        :param password: str — текст, который вводится в поле.
        :return:
        """
        self._driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
