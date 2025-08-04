from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")
search_input = driver.find_element(By.CSS_SELECTOR, "input#username")
search_input.send_keys("tomsmith")
sleep(2)
search_input = driver.find_element(By.CSS_SELECTOR, "input#password")
search_input.send_keys("SuperSecretPassword!")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "button.radius").click()
sleep(2)
print(driver.find_element(By.CSS_SELECTOR, "div#flash.flash.success").text)
sleep(5)
driver.quit()
