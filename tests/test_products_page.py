import allure
import pytest_check as check
from selene import browser, have

from model.pages.products_page import ProductsPage
from model.locators.products_page import ProductsPageLocators


@allure.feature('Products Page')
class TestProductsPage:

    @allure.title('Products page is accessible only when logged in')
    @allure.description('Verify that unauthorized users are redirected to login page when trying to access inventory')
    @allure.story('Access Control')
    def test_products_page_requires_login(self, login_page, products_page):
        with allure.step('open login page'):
            login_page.open()

        with allure.step('try to navigate to inventory page'):
            products_page.open()

        with allure.step('verify redirect to login page'):
            browser.should(have.url('https://www.saucedemo.com/'))

        with allure.step('verify error message is displayed'):
            error_message = login_page.get_error_message()
            assert error_message == "Epic sadface: You can only access '/inventory.html' when you are logged in."

    @allure.title('Products page UI elements are displayed')
    @allure.description('Verify that all main UI elements are visible on the products page')
    @allure.story('UI Validation')
    def test_products_page_ui_elements(self, products_page, logged_in_user):
        with allure.step('verify user is on products page'):
            browser.should(have.url(ProductsPage.URL))

        with allure.step('verify all UI elements are visible'):
            check.is_true(products_page.is_element_visible(ProductsPageLocators.PAGE_TITLE))
            check.is_true(products_page.is_element_visible(ProductsPageLocators.BURGER_MENU_ICON))
            check.is_true(products_page.is_element_visible(ProductsPageLocators.SHOPPING_CART_ICON))
            check.is_true(products_page.is_element_visible(ProductsPageLocators.FILTER_DROPDOWN_MENU))
            check.is_true(products_page.is_element_visible(ProductsPageLocators.PRODUCT_TITLE))
            check.is_true(products_page.is_element_visible(ProductsPageLocators.PRODUCT_PRICE))
            check.is_true(products_page.is_element_visible(ProductsPageLocators.PRODUCT_DESCRIPTION))
            check.is_true(products_page.is_element_visible(ProductsPageLocators.PRODUCT_IMAGE))
            check.is_true(products_page.is_element_visible(ProductsPageLocators.ADD_TO_CART_BUTTON))

    @allure.title('User can add item to cart')
    @allure.description('Verify that user can add a product to shopping cart and counter is updated')
    @allure.story('Shopping Cart')
    def test_add_item_to_cart(self, products_page, logged_in_user):
        with allure.step('verify user is on products page'):
            browser.should(have.url(ProductsPage.URL))

        with allure.step('add Sauce Labs Backpack to cart'):
            products_page.click_add_to_cart('sauce-labs-backpack')

        with allure.step('verify cart counter shows 1'):
            products_page.should_have_cart_counter(1)

        with allure.step('click on shopping cart icon'):
            products_page.click_shopping_cart_icon()

        with allure.step('verify item is in cart'):
            browser.element(ProductsPageLocators.PRODUCT_TITLE).should(have.exact_text('Sauce Labs Backpack'))

    @allure.title('User can remove item from cart')
    @allure.description('Verify that user can remove a product from shopping cart')
    @allure.story('Shopping Cart')
    def test_remove_item_from_cart(self, products_page, logged_in_user):
        with allure.step('verify user is on products page'):
            browser.should(have.url(ProductsPage.URL))

        with allure.step('add Sauce Labs Bike Light to cart'):
            products_page.click_add_to_cart('sauce-labs-bike-light')

        with allure.step('remove Sauce Labs Bike Light from cart'):
            products_page.click_remove_from_cart('sauce-labs-bike-light')

        with allure.step('verify cart counter is not displayed'):
            products_page.should_not_have_cart_counter()

        with allure.step('click on shopping cart icon'):
            products_page.click_shopping_cart_icon()

        with allure.step('verify no items in cart'):
            browser.all(ProductsPageLocators.PRODUCT_TITLE).should(have.size(0))

    @allure.title('User can filter items by name (A-Z)')
    @allure.description('Verify that products are sorted alphabetically from A to Z')
    @allure.story('Product Filtering')
    def test_filter_products_a_to_z(self, products_page, logged_in_user):
        with allure.step('verify user is on products page'):
            browser.should(have.url(ProductsPage.URL))

        with allure.step('select Name (A to Z) filter'):
            products_page.select_filter_option('Name (A to Z)')

        with allure.step('verify products are sorted A to Z'):
            assert products_page.are_products_sorted_ascending()

    @allure.title('User can filter items by name (Z-A)')
    @allure.description('Verify that products are sorted alphabetically from Z to A')
    @allure.story('Product Filtering')
    def test_filter_products_z_to_a(self, products_page, logged_in_user):
        with allure.step('verify user is on products page'):
            browser.should(have.url(ProductsPage.URL))

        with allure.step('select Name (Z to A) filter'):
            products_page.select_filter_option('Name (Z to A)')

        with allure.step('verify products are sorted Z to A'):
            assert products_page.are_products_sorted_descending()

    @allure.title('User can filter items by price (low to high)')
    @allure.description('Verify that products are sorted by price from lowest to highest')
    @allure.story('Product Filtering')
    def test_filter_products_price_low_to_high(self, products_page, logged_in_user):
        with allure.step('verify user is on products page'):
            browser.should(have.url(ProductsPage.URL))

        with allure.step('select Price (low to high) filter'):
            products_page.select_filter_option('Price (low to high)')

        with allure.step('verify products are sorted by price ascending'):
            assert products_page.are_product_prices_sorted_ascending()

    @allure.title('User can filter items by price (high to low)')
    @allure.description('Verify that products are sorted by price from highest to lowest')
    @allure.story('Product Filtering')
    def test_filter_products_price_high_to_low(self, products_page, logged_in_user):
        with allure.step('verify user is on products page'):
            browser.should(have.url(ProductsPage.URL))

        with allure.step('select Price (high to low) filter'):
            products_page.select_filter_option('Price (high to low)')

        with allure.step('verify products are sorted by price descending'):
            assert products_page.are_product_prices_sorted_descending()