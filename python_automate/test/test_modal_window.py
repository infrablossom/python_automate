from functions import *


def test_modal_window():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/three_buttons')
        confirm_button = wait_until_clickable(browser, (By.XPATH, '//*[contains(text(), "Confirm")]'))
        confirm_button.click()
        alert = WebDriverWait(browser, 5).until(ec.alert_is_present())
        alert.dismiss()
        text = browser.find_element_by_id('confirm_text').text
        assert text == 'Не запускаем', f'Некорректный текст: {text}'