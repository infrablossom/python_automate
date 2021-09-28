from functions import *


def test_iframe():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/iframe_page')
        wait = WebDriverWait(browser, 5)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.ID, 'my_iframe')))
        wait_until_visible(browser, (By.ID, 'photo'))
        confirm_btn = wait_until_clickable(browser, (By.XPATH, '//*[contains(text(), "Подтвердить")]'))
        confirm_btn.click()
        alert = WebDriverWait(browser, 5).until(ec.alert_is_present())
        alert.accept()
        browser.switch_to.default_content()
