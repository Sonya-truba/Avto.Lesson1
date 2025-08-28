from selenium.webdriver.common.by import By


class Auth:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def auth(self, login, password):
        self._driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "input#login-button").click()
