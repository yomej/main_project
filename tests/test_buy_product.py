from selenium import webdriver
from pages.login_page import LoginPage


def test_login():
    driver = webdriver.Chrome()
    print("start test 1")

    login = LoginPage(driver)
    login.authorization()


