from functions import *
from functions import element_is_present


def test_inputs_page():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/inputs')
        input_test = browser.find_element_by_xpath("//*[@name='test']")
        input_test.send_keys("Some text")
        button = browser.find_element_by_xpath("//*[@name='test']/following::button")
        button.click()
        assert element_is_present(browser, (By.XPATH, "//*[@class='notification is-success']")), \
            "Сообщение об успехе отсутствует"
        success_text = browser.find_element_by_xpath("//*[@class='notification is-success']").text
        assert success_text == "Верно", f"Неверное сообщение об успехе: {success_text}"
