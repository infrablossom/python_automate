from functions import *


def test_timer_page():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/wait')
        wait = WebDriverWait(browser, 10, poll_frequency=0.3)
        wait.until(ec.text_to_be_present_in_element((By.XPATH, '//*[@id="demo"]'), '100'))
        button = wait_until_clickable(browser, (By.XPATH, '//*[@onclick="check_value()"]'))
        button.click()
        check_alert_is_present(browser)
