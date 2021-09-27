from selenium.webdriver import Chrome
from functions import cookie_login


def test_open_stand():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/inputs')
