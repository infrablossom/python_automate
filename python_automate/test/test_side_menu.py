from selenium.webdriver import Chrome
from functions import login


def test_side_menu():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/')
        browser.maximize_window()
        login_button = browser.find_element_by_xpath('//*[contains(text(), "Вход")]')
        login_button.click()
        login(browser)
        expected_names = ['Поля ввода и кнопки', 'Мой питомец', 'О себе',
                          'Загрузка файла', 'Ожидание', 'Медленная загрузка', 'Модальные окна', 'Новая вкладка',
                          'iframe', 'Drag-and-drop']
        sidebar_names = [sidebar_item.text for sidebar_item in
                         browser.find_elements_by_xpath('//li/a[@class="navbar-item"]')]
        assert sidebar_names == expected_names, f"Неверные названия пунктов бокового меню: {sidebar_names}"
