from selenium.webdriver import Chrome
from functions import login


def test_open_stand():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/inputs')
        browser.maximize_window()
        login(browser)
