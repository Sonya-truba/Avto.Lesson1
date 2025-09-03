from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:

    def __init__(self, driver):
        """
         Конструктор класса CalcMainPage.
        :param driver: WebDriver — объект драйвера Selenium.
         """
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step("Заполнение формы.")
    def fill_personal_data(self, name, family, address, mail, phone, code, city, country, job, company):
        """
        Заполняет поля личными данными.
        :param name: str — текст, который вводится в поле.
        :param family: str — текст, который вводится в поле.
        :param address: str — текст, который вводится в поле.
        :param mail: str — текст, который вводится в поле.
        :param phone: str — текст, который вводится в поле.
        :param code: str — текст, который вводится в поле.
        :param city: str — текст, который вводится в поле.
        :param country: str — текст, который вводится в поле.
        :param job: str — текст, который вводится в поле.
        :param company: str — текст, который вводится в поле.
        :return: str

        """
        self._driver.find_element(By.NAME, "first-name").send_keys(name)
        self._driver.find_element(By.NAME, "last-name").send_keys(family)
        self._driver.find_element(By.NAME, "address").send_keys(address)
        self._driver.find_element(By.NAME, "e-mail").send_keys(mail)
        self._driver.find_element(By.NAME, "phone").send_keys(phone)
        self._driver.find_element(By.NAME, "zip-code").send_keys(code)
        self._driver.find_element(By.NAME, "city").send_keys(city)
        self._driver.find_element(By.NAME, "country").send_keys(country)
        self._driver.find_element(By.NAME, "job-position").send_keys(job)
        self._driver.find_element(By.NAME, "company").send_keys(company)

    @allure.step("Подтверждение отправки формы.")
    def click_submit_button(self):
        """
        Нажимает кнопку подтверждения и отправки данных 'Submit'.
        :return: str
        """
        WebDriverWait(self._driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
        self._driver.find_element(By.CSS_SELECTOR, "button").click()
