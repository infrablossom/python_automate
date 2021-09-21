from functions import *


def test_of_navigation():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/profile')
        wait = WebDriverWait(browser, 5)
        browser.maximize_window()
        login(browser)
        my_pet = browser.find_element_by_xpath('//*[@href="/my_pet"]')
        my_pet.click()
        wait.until(ec.url_to_be('https://qastand.valhalla.pw/my_pet'))
        browser.refresh()
        assert wait.until(ec.title_is('Course Test Stand')), 'Некорректный заголовок страницы'

