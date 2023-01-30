from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base.base_class import BasePage


class LoginPage(BasePage):
    url = "https://www.dns-shop.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_button = ".base-ui-button-v2_white.base-ui-button-v2_ico-none"
    swich_to_password = ".block-other-login-methods__password-caption"
    login_form = "//input[@autocomplete='username']"
    password = "//input[@autocomplete='current-password']"
    big_login_button = ".base-ui-button-v2_big"

    # Getters
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_button)))

    def get_swich_to_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.swich_to_password)))

    def get_login_form(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_form)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_big_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.big_login_button)))

    # Actions

    def click_login_button(self):
        self.get_login_button().click()
        print("click login button")

    def click_swich_to_password(self):
        self.get_swich_to_password().click()
        print("switch message to password")

    def input_login(self, login):
        self.get_login_form().send_keys(login)
        print("login form filling")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("filling password form")

    def click_big_login_button(self):
        self.get_big_login_button().click()
        print("click big login button")
        print("success log in")

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_login_button()
        self.click_swich_to_password()
        self.input_login('79136984482')
        self.input_password('niKG0dJ4')
        self.click_big_login_button()