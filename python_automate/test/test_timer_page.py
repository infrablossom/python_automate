from functions import *


def test_timer_page():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/wait')
        wait = WebDriverWait(browser, 20)
        browser.maximize_window()
        login(browser)
        wait.until(ec.text_to_be_present_in_element((By.XPATH, '//*[@id="demo"]'), '100'))
