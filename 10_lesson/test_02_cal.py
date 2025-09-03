import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from InputData import InputData
import allure


@allure.title("Тестирование калькулятора.")
@allure.description("Тест проверяет корректность работы калькулятора с задержкой 45 cекунд.")
@allure.feature("Калькулятор.")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Открытие главной страницы в браузере."):
        input_data = InputData(driver)
    with allure.step("Установка задержки 45 секунд."):
        input_data.delay(45)
    with allure.step("Объявление начала загрузки."):
        start_time = time.time()
    with allure.step("Нажатие кнопок '7', '+','8', '='."):
        input_data.press_calculation_button("//span[text()='7']")
        input_data.press_calculation_button("//span[text()='+']")
        input_data.press_calculation_button("//span[text()='8']")
        input_data.press_calculation_button("//span[text()='=']")
    with allure.step("Ожидание появления '15' в поле вывода итогового значения."):
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    with allure.step("Объявление конца загрузки."):
        end_time = time.time()
    with allure.step("Проверка времени загрузки."):
        load_time = end_time - start_time
        assert 43 <= load_time <= 47
    with allure.step("Закрытие браузера."):
        driver.quit()
