from functions import *


def test_new_tab():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/new_window_button')
        tab = browser.window_handles
        assert len(tab) == 1, f'Должна быть открыта 1 вкладка, но открылось: {len(tab)}'
        new_tab_btn = wait_until_clickable(browser, (By.XPATH, '//*[contains(text(), "Открыть")]'))
        new_tab_btn.click()
        tab_2 = browser.window_handles
        browser.switch_to.window(tab_2[1])
        assert len(tab_2) == 2, f'Должно быть открыто 2 вкладки, но открылось: {len(tab_2)}'
        send = wait_until_clickable(browser, (By.XPATH, '//*[contains(text(), "Отправить")]'))
        send.click()
        alert = WebDriverWait(browser, 5).until(ec.alert_is_present())
        alert.accept()
        #добавила явное ожидание, когда будет 1 вкладка
        #иногда тест падает, потому что считает вкладки до закрытия второй
        WebDriverWait(browser, 5).until(ec.number_of_windows_to_be(1))
        tab_3 = browser.window_handles
        assert len(tab_3) == 1, f'Должна быть открыта 1 вкладка, но открылось: {len(tab_3)}'



