import allure
import pytest
from selene import browser, have

from model.pages.login_page import LoginPage


@pytest.fixture
def login_page(set_browser):
    return LoginPage()


@allure.feature('Login')
class TestLogin:

    @allure.title('Login succeeds with correct username and password')
    @allure.description('This test verifies that user can successfully login with valid credentials')
    @allure.story('Successful Login')
    def test_login_with_valid_credentials(self, login_page):
        with allure.step('open login page'):
            login_page.open()

        with allure.step('enter valid username'):
            login_page.enter_username('standard_user')

        with allure.step('enter valid password'):
            login_page.enter_password('secret_sauce')

        with allure.step('click login button'):
            login_page.press_login_button()

        with allure.step('verify user is redirected to products page'):
            browser.should(have.url('https://www.saucedemo.com/inventory.html'))

    @allure.title('Login fails with incorrect username')
    @allure.description('This test verifies that login fails when incorrect username is provided')
    @allure.story('Failed Login')
    def test_login_with_incorrect_username(self, login_page):
        with allure.step('open login page'):
            login_page.open()

        with allure.step('enter incorrect username'):
            login_page.enter_username('wrong_user')

        with allure.step('enter valid password'):
            login_page.enter_password('secret_sauce')

        with allure.step('click login button'):
            login_page.press_login_button()

        with allure.step('verify error message is displayed'):
            error_message = login_page.get_error_message()
            assert error_message == "Epic sadface: Username and password do not match any user in this service"

    @allure.title('Login fails with empty username')
    @allure.description('This test verifies that login fails when username field is empty')
    @allure.story('Failed Login')
    def test_login_with_empty_username(self, login_page):
        with allure.step('open login page'):
            login_page.open()

        with allure.step('enter password only'):
            login_page.enter_password('secret_sauce')

        with allure.step('click login button'):
            login_page.press_login_button()

        with allure.step('verify error message is displayed'):
            error_message = login_page.get_error_message()
            assert error_message == "Epic sadface: Username is required"

    @allure.title('Login fails with incorrect password')
    @allure.description('This test verifies that login fails when incorrect password is provided')
    @allure.story('Failed Login')
    def test_login_with_incorrect_password(self, login_page):
        with allure.step('open login page'):
            login_page.open()

        with allure.step('enter valid username'):
            login_page.enter_username('standard_user')

        with allure.step('enter incorrect password'):
            login_page.enter_password('super_secret_sauce')

        with allure.step('click login button'):
            login_page.press_login_button()

        with allure.step('verify error message is displayed'):
            error_message = login_page.get_error_message()
            assert error_message == "Epic sadface: Username and password do not match any user in this service"

    @allure.title('Login fails with empty password')
    @allure.description('This test verifies that login fails when password field is empty')
    @allure.story('Failed Login')
    def test_login_with_empty_password(self, login_page):
        with allure.step('open login page'):
            login_page.open()

        with allure.step('enter username only'):
            login_page.enter_username('standard_user')

        with allure.step('click login button'):
            login_page.press_login_button()

        with allure.step('verify error message is displayed'):
            error_message = login_page.get_error_message()
            assert error_message == "Epic sadface: Password is required"

    @allure.title('Login fails for locked out user')
    @allure.description('This test verifies that locked out user cannot login')
    @allure.story('Failed Login')
    def test_login_with_locked_out_user(self, login_page):
        with allure.step('open login page'):
            login_page.open()

        with allure.step('enter locked out username'):
            login_page.enter_username('locked_out_user')

        with allure.step('enter valid password'):
            login_page.enter_password('secret_sauce')

        with allure.step('click login button'):
            login_page.press_login_button()

        with allure.step('verify error message is displayed'):
            error_message = login_page.get_error_message()
            assert error_message == "Epic sadface: Sorry, this user has been locked out."