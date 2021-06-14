from PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By


class RyanAirSearchSelectors:

    input = "//input[@id='input-button__destination']"
    first_flight_date = "//div[@data-id='2021-07-05']"
    second_flight_date = "//div[@data-id='2021-07-09']"
    search = "//button[@data-ref='flight-search-widget__cta']"
    berlin_suggestion = "//span[@data-id='BER']"
    accept_cookies = "//button[contains(concat(' ', @class, ' '), ' cookie-popup-with-overlay__button ')][" \
                     "@data-ref='cookie.accept-all'] "
    no_charge_fee_selector = "//div[contains(concat(' ', @class, ' '), ' free-card__content ')]"
    kyiv_departure = "//h4[contains(text(), 'Київ-Бориспіль')]"
    berlin_arrival = "//h4[contains(text(), 'Берлін-Бранденбург')]"
    flight_number = "//div[contains(text(), '5404')]"


class RyanAirPageObject(BasePage):

    def accept_cookies(self):
        return self.find_element(RyanAirSearchSelectors.accept_cookies).click()

    def enter_word(self, word):
        search_field = self.find_element(RyanAirSearchSelectors.input)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def select_berlin(self):
        return self.find_element(RyanAirSearchSelectors.berlin_suggestion).click()

    def choose_flight_date(self, flight):
        if flight == 1:
            return self.find_element(RyanAirSearchSelectors.first_flight_date).click()
        elif flight == 2:
            return self.find_element(RyanAirSearchSelectors.second_flight_date).click()

    def click_on_the_search_button(self):
        return self.find_element(RyanAirSearchSelectors.search).click()

    def fill_in_search_form(self, word):
        self.enter_word(word)
        self.select_berlin()
        self.choose_flight_date(1)
        self.choose_flight_date(2)

    def find_no_charge_fee(self):
        no_charge_fee = self.find_element(RyanAirSearchSelectors.no_charge_fee_selector)
        no_charge_text = no_charge_fee.text
        return no_charge_text

    def find_kyiv_departure(self):
        return self.find_element(RyanAirSearchSelectors.kyiv_departure).text

    def find_berlin_arrival(self):
        return self.find_element(RyanAirSearchSelectors.berlin_arrival).text

    def find_flight_number(self):
        return self.find_element(RyanAirSearchSelectors.flight_number).text
