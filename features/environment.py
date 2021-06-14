from selenium import webdriver
from behave import fixture, use_fixture
from PageObjects.GooglePageObject import GooglePageObject
from PageObjects.RyanAirPageObject import RyanAirPageObject
from webdriver_manager.chrome import ChromeDriverManager


@fixture()
def browser_chrome(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    context.google = GooglePageObject(driver)
    context.ryanair = RyanAirPageObject(driver)
    yield driver
    driver.quit()


def before_all(context):
    use_fixture(browser_chrome, context)
