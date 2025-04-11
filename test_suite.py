import pytest
from selenium import webdriver

from Action.Action_Page import ActionPage


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = ActionPage(driver)
    login_page.open_login_page("https://www.saucedemo.com/")
    return login_page

#Log in page
def test_login_page_on_sauce_demo_website(login):
    login.enter_username("visual_user")
    login.enter_password("secret_sauce")
    login.click_submit_button()