from selene import browser, query
from model.locators.login_page import LoginPageLocators


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def open(self):
        browser.open(self.URL)
        return self

    def enter_username(self, username):
        browser.element(LoginPageLocators.USERNAME_INPUT).clear().type(username)
        return self

    def enter_password(self, password):
        browser.element(LoginPageLocators.PASSWORD_INPUT).clear().type(password)
        return self

    def press_login_button(self):
        browser.element(LoginPageLocators.LOGIN_BUTTON).click()
        return self

    def get_error_message(self):
        return browser.element(LoginPageLocators.ERROR_MESSAGE).get(query.text)