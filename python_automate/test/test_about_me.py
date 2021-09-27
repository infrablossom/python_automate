from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from functions import *


def test_about_me():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/about')
        name = browser.find_element_by_xpath('//*[@name="name"]')
        surname = browser.find_element_by_xpath('//*[@name="surname"]')
        name.send_keys('Tanya')
        surname.send_keys('Ohlsen')
        manual_button = browser.find_element_by_xpath('//*[@id="age1"]')
        assert manual_button.get_attribute("checked"), "Чекбокс по умолчанию не включен"

        auto_button = browser.find_element_by_xpath('//*[@id="age2"]')
        auto_button.click()

        py_checkbox = browser.find_element_by_xpath('//*[@value="Python"]')
        py_checkbox.click()

        lvl = browser.find_element_by_xpath('//*[@id="lvl"]')
        select = Select(lvl)
        select.select_by_visible_text('Junior')

        name.send_keys(Keys.ENTER)
        assert element_is_present(browser, (By.XPATH, '//*[@class="notification is-success"]')), \
            "Сообщение об успехе отсутствует"