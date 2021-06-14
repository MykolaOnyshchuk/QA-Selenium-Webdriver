from PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By


class GoogleSearchSelectors:

    input_field = "//input[@title='Пошук']"
    search_button = "//div[@jsname]/center/input[@name='btnK']"
    results_quantity = "//div[contains(text(), 'Приблизна кількість результатів:')]"
    ryanair_link = "//a[@href='https://www.ryanair.com/ua/uk/']/h3"


class GooglePageObject(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSearchSelectors.input_field)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(GoogleSearchSelectors.search_button).click()

    def search(self, word):
        self.enter_word(word)
        self.click_on_the_search_button()

    def enter_ryanair(self):
        return self.find_element(GoogleSearchSelectors.ryanair_link).click()

    def return_results_quantity(self):
        return self.find_element(GoogleSearchSelectors.results_quantity).text
