import datetime


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Value word is correct")

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('/home/merg/PycharmProjects/pythonProject/screen/' + name_screenshot)

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Url is correct")