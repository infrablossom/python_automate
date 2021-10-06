import os
from functions import *
from functions import element_is_present

def test_upload_file():
    with Chrome() as browser:
        cookie_login(browser)
        browser.get('https://qastand.valhalla.pw/upload_file')
        upload = browser.find_element_by_xpath('//*[@name="file"]')
        wtf = os.path.join(os.getcwd(), 'resources', 'harley.jpg')
        print(wtf)
        upload.send_keys(os.path.join(os.getcwd(), 'resources', 'harley.jpg'))
        submit = browser.find_element_by_xpath('//*[@type="submit"]')
        submit.click()

        assert element_is_present(browser, (By.XPATH, '//*[@class="notification is-success"]')), \
            "Сообщение об успехе отсутствует"
        browser.refresh()
        assert not element_is_present(browser, (By.XPATH, '//*[@class="notification is-success"]')), \
            "Сообщение об успехе отсутствует"


