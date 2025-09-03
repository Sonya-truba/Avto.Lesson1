from selenium.webdriver.common.by import By
import allure


class DataPage:
    @allure.step("Соответствие зеленому цвету.")
    def check_green_color_background(self, driver, selector):
        """
        Проверка поля на соответствие зеленому цвету.
        :param driver: WebDriver — объект драйвера Selenium.
        :param selector: str - название кнопки с использованием CSS-selector
        :return: str
        """
        green_color = "rgba(209, 231, 221, 1)"
        element = driver.find_element(By.CSS_SELECTOR, selector)
        actual_col = element.value_of_css_property("background-color")
        assert actual_col == green_color

    @allure.step("Соответствие красному цвету.")
    def check_red_color_background(self, driver, selector):
        """
        Проверка поля на соответствие красному цвету.
        :param driver: WebDriver — объект драйвера Selenium.
        :param selector: str - название кнопки с использованием CSS-selector
        :return: str
        """
        red_color = "rgba(248, 215, 218, 1)"
        element = driver.find_element(By.CSS_SELECTOR, selector)
        actual_col = element.value_of_css_property("background-color")
        assert actual_col == red_color
