from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import login
from functions import element_is_present


class Test_My_Pet():

    def test_my_pet_positive(self):
        with Chrome() as browser:
            browser.get('https://qastand.valhalla.pw/my_pet')
            browser.maximize_window()
            login(browser)
            pet = browser.find_element_by_xpath('//*[@name="pet"]')
            pet.send_keys('Кот')
            name = browser.find_element_by_xpath('//*[@name="name"]')
            name.send_keys('Зефир')
            age = browser.find_element_by_xpath('//*[@name="age"]')
            age.send_keys('3')
            sex = browser.find_element_by_xpath('//*[@name="sex"]')
            sex.send_keys('Мужской')
            submit = browser.find_element_by_xpath('//*[contains(text(), "Подтвердить")]')
            submit.click()
            assert element_is_present(browser, By.XPATH, '//*[@class="notification is-success"]'), \
                "Сообщение об успехе отсутствует"
            success_text = browser.find_element_by_xpath('//*[@class="notification is-success"]').text
            assert success_text == "Успех.", f"Неверное сообщение об успехе: {success_text}"

    def test_my_pet_negative(self):
        with Chrome() as browser:
            browser.get('https://qastand.valhalla.pw/my_pet')
            browser.maximize_window()
            login(browser)
            pet = browser.find_element_by_xpath('//*[@name="pet"]')
            pet.send_keys('Кот')
            submit = browser.find_element_by_xpath('//*[contains(text(), "Подтвердить")]')
            submit.click()
            assert element_is_present(browser, By.XPATH, '//*[@class="notification is-danger"]'), \
                "Сообщение о неудаче отсутствует"
            fail_text = browser.find_element_by_xpath('//*[@class="notification is-danger"]').text
            assert fail_text == "Заполнены не все поля.", f"Неверное сообщение о неудаче: {fail_text}"
