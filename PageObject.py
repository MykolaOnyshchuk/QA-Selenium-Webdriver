from BaseApp import BasePage
from selenium.webdriver.common.by import By


class RyanAirSearchLocators:

    input = (By.XPATH, "//input[@id='input-button__destination']")
    FIRST_FLIGHT_DATE = (By.XPATH, "//div[@data-id='2021-07-05']")
    SECOND_FLIGHT_DATE = (By.XPATH, "//div[@data-id='2021-07-09']")
    SEARCH = (By.XPATH, "//button[@data-ref='flight-search-widget__cta']")
    berlin_suggestion = (By.XPATH, "//span[@data-id='BER']")
    accept_cookies = (By.XPATH, "//button[contains(concat(' ', @class, ' '), ' cookie-popup-with-overlay__button ')]["
                                "@data-ref='cookie.accept-all']")
    no_charge_fee_selector = (By.XPATH, "//div[contains(concat(' ', @class, ' '), ' free-card__content ')]")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(RyanAirSearchLocators.input)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def select_berlin(self):
        return self.find_element(RyanAirSearchLocators.berlin_suggestion, time=2).click()

    def choose_flight_date(self, flight):
        if flight == 1:
            return self.find_element(RyanAirSearchLocators.FIRST_FLIGHT_DATE, time=5).click()
        elif flight == 2:
            return self.find_element(RyanAirSearchLocators.SECOND_FLIGHT_DATE, time=5).click()

    def click_on_the_search_button(self):
        return self.find_element(RyanAirSearchLocators.SEARCH, time=5).click()

    def accept_cookies(self):
        return self.find_element(RyanAirSearchLocators.accept_cookies, time=5).click()

    def find_no_charge_fee(self):
        no_charge_fee = self.find_element(RyanAirSearchLocators.no_charge_fee_selector, time=15)
        no_charge_text = no_charge_fee.text
        return no_charge_text
