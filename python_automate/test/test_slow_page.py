from functions import *

def test_slow_page():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/slow_load')
        browser.maximize_window()
        login(browser)
        text_input = wait_until_clickable(browser, By.XPATH, '//*[@id="text_input"]')
        text_input.send_keys('Some text')
        button = wait_until_clickable(browser, By.XPATH, '//*[@id="button"]')
        button.click()
        assert element_is_present(browser, By.XPATH, '//*[@class="notification is-success"]'), \
            "Сообщение об успехе отсутствует"
        browser.refresh()
        assert not element_is_present(browser, By.XPATH, '//*[@class="notification is-success"]'), \
            "Сообщение об успехе не исчезло"
