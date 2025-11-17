import allure
from selene import browser, have


@allure.feature('Shopping Cart')
class TestShoppingCart:

    @allure.title('Checkout page is accessible only when logged in')
    @allure.description('Verify that unauthorized users are redirected to login page when trying to access checkout')
    @allure.story('Access Control')
    def test_checkout_page_requires_login(self, login_page, shopping_cart_page):
        with allure.step('open login page'):
            login_page.open()

        with allure.step('try to navigate to shopping cart page'):
            shopping_cart_page.open()

        with allure.step('verify redirect to login page'):
            browser.should(have.url('https://www.saucedemo.com/'))

        with allure.step('verify error message is displayed'):
            error_message = login_page.get_error_message()
            assert error_message == "Epic sadface: You can only access '/cart.html' when you are logged in."