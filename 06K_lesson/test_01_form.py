from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_data_types():

    options = Options()
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    options.add_argument('--start-maximized')
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Заполнение полей страницы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина,55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("Skypro")

    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
    )
    driver.find_element(By.CSS_SELECTOR, "button").click()

    green_color = "rgba(209, 231, 221, 1)"
    red_color = "rgba(248, 215, 218, 1)"

    selector = ["div#first-name", "div#last-name", "div#address", "div#e-mail", "div#phone", "div#zip-code", "div#city", "div#country", "div#job-position", "div#company"]
    for selector in selector:
        element = driver.find_element(By.CSS_SELECTOR, selector)
        actual_col = element.value_of_css_property("background-color")
        if "zip-code" in selector:
            expected_color = red_color

        else:
            expected_color = green_color

        assert actual_col == expected_color

    driver.quit()
