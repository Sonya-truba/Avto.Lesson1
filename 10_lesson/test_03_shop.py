from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from auth import Auth
from MainPageShop import MainPage
from CheckOut import CheckOut
from Order import Order
import allure


@allure.title("Тестирование магазина.")
@allure.description("Тест проверяет соответствие действительной и указанной в счете общей стоимости заказа.")
@allure.feature("Магазин.")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    with allure.step("Открытие страницы авторизации в браузере."):
        auth = Auth(driver)
    with allure.step("Авторизация. Ввод данных для авторизации."):
        auth.login_with_credentials("standard_user", "secret_sauce")
    with allure.step("Переход на главную страницу."):
        main_page = MainPage(driver)
    with allure.step("Выбор различных позиций товаров. Заполнение корзины."):
        main_page.shopping("button#add-to-cart-sauce-labs-backpack")
        main_page.shopping("button#add-to-cart-sauce-labs-bolt-t-shirt")
        main_page.shopping("button#add-to-cart-sauce-labs-onesie")
        main_page.click_buy_button()
    with allure.step("Переход в корзину."):
        check_out = CheckOut(driver)
        check_out.click_check_out_button()
    with allure.step("Переход на страницу оформления заказа. Ввод личных данных."):
        order = Order(driver)
        order.fill_order_form("Иван", "Петров", "123456")
    with allure.step("Проверка соответствия итоговой стоимости."):
        assert order.summary_total() == "Total: $58.29"
    with allure.step("Закрытие браузера."):
        driver.quit()
