from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageForm import MainPage
from DataPage import DataPage
import allure


@allure.title("Тестирование цвета поля после его заполнение и подтверждения.")
@allure.description("Тест проверяет подсвечивание поля красным при вводе пустого значения.")
@allure.feature("Форма заполнения личных данных.")
@allure.severity("CRITICAL")
def test_data_types():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Открытие главной страницы в браузере."):
        main_page = MainPage(driver)
    with allure.step("Ввод личных данных в поля на странице."):
        main_page.fill_personal_data("Иван", "Петров", "Ленина,55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "Skypro")
        main_page.click_submit_button()
    with allure.step("Переход на страницу с заполненными данными."):
        data_page = DataPage()
    with allure.step("Проверка поля на соответствие цвету."):
        data_page.check_green_color_background(driver, "div#first-name")
        data_page.check_green_color_background(driver, "div#last-name")
        data_page.check_green_color_background(driver, "div#address",)
        data_page.check_green_color_background(driver, "div#e-mail")
        data_page.check_green_color_background(driver, "div#phone")
        data_page.check_red_color_background(driver, "div#zip-code")
        data_page.check_green_color_background(driver, "div#city")
        data_page.check_green_color_background(driver, "div#country")
        data_page.check_green_color_background(driver, "div#job-position")
        data_page.check_green_color_background(driver, "div#company")
    with allure.step("Закрытие браузера."):
        driver.quit()
