from behave import *


@given("a customer enters a browser")
def search_ryanair(context):
    context.google.go_to_site()
    context.google.search("ryanair")


@when("a customer clicks ryanair website link")
def enter_ryanair_website(context):
    assert "Приблизна кількість результатів" in context.google.return_results_quantity()
    context.google.enter_ryanair()
    context.ryanair.accept_cookies()


@when("sends a filled search form")
def send_filled_search_form(context):
    context.ryanair.fill_in_search_form("Берлін")
    context.ryanair.click_on_the_search_button()


@then("the customer finds the tickets if they are available")
def find_tickets(context):
    assert "Бронюйте до 30 вересня" in context.ryanair.find_no_charge_fee()
    assert "Київ-Бориспіль" in context.ryanair.find_kyiv_departure()
    assert "Берлін-Бранденбург" in context.ryanair.find_berlin_arrival()
    assert "FR 5404" in context.ryanair.find_flight_number()
