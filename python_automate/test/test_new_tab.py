from functions import *


def test_new_tab():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/new_window_button')
        tabs = browser.window_handles
        assert len(tabs) == 1, f'Должна быть открыта 1 вкладка, но открылось: {len(tabs)}'
        new_tab_btn = wait_until_clickable(browser, (By.XPATH, '//*[contains(text(), "Открыть")]'))
        new_tab_btn.click()
        tabs = browser.window_handles
        browser.switch_to.window(tabs[1])
        assert len(tabs) == 2, f'Должно быть открыто 2 вкладки, но открылось: {len(tabs)}'
        send = wait_until_clickable(browser, (By.XPATH, '//*[contains(text(), "Отправить")]'))
        send.click()
        alert = WebDriverWait(browser, 5).until(ec.alert_is_present())
        alert.accept()
        WebDriverWait(browser, 5).until(ec.number_of_windows_to_be(1))
        tabs = browser.window_handles
        assert len(tabs) == 1, f'Должна быть открыта 1 вкладка, но открылось: {len(tabs)}'
