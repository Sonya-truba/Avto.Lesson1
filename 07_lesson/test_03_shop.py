from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from auth import Auth
from MainPageShop import MainPage
from CheckOut import CheckOut
from Order import Order


def test_saucedemo():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    auth = Auth(driver)
    auth.auth("standard_user", "secret_sauce")
    main_page = MainPage(driver)
    main_page.shopping(driver, "button#add-to-cart-sauce-labs-backpack")
    main_page.shopping(driver, "button#add-to-cart-sauce-labs-bolt-t-shirt")
    main_page.shopping(driver, "button#add-to-cart-sauce-labs-onesie")
    main_page.buy()
    check_out = CheckOut(driver)
    check_out.check_out(driver)
    order = Order(driver)
    order.order(driver, "Иван", "Петров", "123456")
    order.total()
    assert order.total() == "Total: $58.29"
    driver.quit()
