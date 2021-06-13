from PageObject import SearchHelper
from conftest import browser


ryanair_main_page = SearchHelper(browser)
ryanair_main_page.go_to_site()
ryanair_main_page.accept_cookies()
ryanair_main_page.enter_word("Берлін-Бранденбург")
ryanair_main_page.select_berlin()
ryanair_main_page.choose_flight_date(1)
ryanair_main_page.choose_flight_date(2)
ryanair_main_page.click_on_the_search_button()
no_charge_fee = ryanair_main_page.find_no_charge_fee()
assert "Бронюйте до 30 вересня" in no_charge_fee
