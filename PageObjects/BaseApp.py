from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.google.com.ua"

    def find_element(self, selector):
        return self.driver.find_element_by_xpath(selector)

    def go_to_site(self):
        return self.driver.get(self.base_url)
