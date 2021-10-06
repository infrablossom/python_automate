from functions import *


def test_of_navigation():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/profile')
        wait = WebDriverWait(browser, 5)
        my_pet = browser.find_element_by_xpath('//*[@href="/my_pet"]')
        my_pet.click()
        wait.until(ec.url_to_be('https://qastand.valhalla.pw/my_pet'))
        browser.refresh()
        assert wait.until(ec.title_is('Course Test Stand')), 'Некорректный заголовок страницы'

