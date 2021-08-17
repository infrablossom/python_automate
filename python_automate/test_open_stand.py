from selenium.webdriver import Chrome

def test_open_stand():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/')
        print(f'{browser.current_url} is open')