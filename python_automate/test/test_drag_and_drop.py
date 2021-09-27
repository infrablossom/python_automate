from functions import *


def test_drag_and_drop():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/drag_and_drop_page')
        koala = wait_until_clickable(browser, (By.ID, 'draggable'))
        square = wait_until_clickable(browser, (By.ID, 'droppable'))
        ActionChains(browser).drag_and_drop(koala, square).perform()
        success_text = wait_until_visible(browser, (By.XPATH, '//*[@id="droppable"]//p')).text

        assert success_text == 'Успех!', f'Некорректное сообщение об успехе: {success_text}'
