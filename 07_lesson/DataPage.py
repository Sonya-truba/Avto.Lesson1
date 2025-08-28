from selenium.webdriver.common.by import By


class DataPage:

    def check_green(self, driver, selector):
        green_color = "rgba(209, 231, 221, 1)"
        element = driver.find_element(By.CSS_SELECTOR, selector)
        actual_col = element.value_of_css_property("background-color")
        assert actual_col == green_color

    def check_red(self, driver, selector):
        red_color = "rgba(248, 215, 218, 1)"
        element = driver.find_element(By.CSS_SELECTOR, selector)
        actual_col = element.value_of_css_property("background-color")
        assert actual_col == red_color
