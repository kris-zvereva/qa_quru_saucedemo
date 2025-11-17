from selene import browser, be, have
from model.locators.shopping_cart import ShoppingCartPageLocators


class ShoppingCartPage:
    URL = "https://www.saucedemo.com/cart.html"

    def open(self):
        browser.open(self.URL)
        return self

    def is_element_visible(self, locator):
        return browser.element(locator).matching(be.visible)

    def is_item_in_cart(self, product_title):
        """Check if item with specific title is present in cart"""
        locator = f'//div[@class="inventory_item_name" and contains(text(), "{product_title}")]'
        return browser.element(locator).matching(be.visible)

    def is_item_not_in_cart(self, product_title):
        """Check if item with specific title is NOT present in cart"""
        locator = f'//div[@class="inventory_item_name" and contains(text(), "{product_title}")]'
        return not browser.element(locator).matching(be.visible)

    def click_continue_shopping(self):
        browser.element(ShoppingCartPageLocators.CONTINUE_SHOPPING_BUTTON).click()
        return self

    def click_checkout(self):
        browser.element(ShoppingCartPageLocators.CHECKOUT_BUTTON).click()
        return self

    def click_remove_button(self, product_name):
        browser.element(f'[data-test="remove-{product_name}"]').click()
        return self

    def get_cart_items_count(self):
        return len(browser.all(ShoppingCartPageLocators.CART_ITEM))