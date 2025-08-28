from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageForm import MainPage
from DataPage import DataPage


def test_data_types():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.data("Иван", "Петров", "Ленина,55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "Skypro")
    main_page.submit(driver)
    data_page = DataPage()
    data_page.check_green(driver, "div#first-name")
    data_page.check_green(driver, "div#last-name")
    data_page.check_green(driver, "div#address",)
    data_page.check_green(driver, "div#e-mail")
    data_page.check_green(driver, "div#phone")
    data_page.check_red(driver, "div#zip-code")
    data_page.check_green(driver, "div#city")
    data_page.check_green(driver, "div#country")
    data_page.check_green(driver, "div#job-position")
    data_page.check_green(driver, "div#company")
    driver.quit()
