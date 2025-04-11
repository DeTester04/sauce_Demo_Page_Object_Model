import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locators.Locators_page import LoginLocators


class ActionPage:
    #Initializing our browser
    def __init__(self, driver):
        self.driver = driver

#calling our URL
    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.USERNAME))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(5)

