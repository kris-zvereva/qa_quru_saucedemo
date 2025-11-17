from selene import browser, be, query, have
from model.locators.products_page import ProductsPageLocators


class ProductsPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def open(self):
        browser.open(self.URL)
        return self

    def is_element_visible(self, locator):
        return browser.element(locator).matching(be.visible)

    def click_add_to_cart(self, product_name):
        browser.element(f'[data-test="add-to-cart-{product_name}"]').click()
        return self

    def click_remove_from_cart(self, product_name):
        browser.element(f'[data-test="remove-{product_name}"]').click()
        return self

    def click_shopping_cart_icon(self):
        browser.element(ProductsPageLocators.SHOPPING_CART_ICON).click()
        return self

    def select_filter_option(self, filter_name):
        filter_map = {
            "Name (A to Z)": ProductsPageLocators.FILTER_AZ_OPTION,
            "Name (Z to A)": ProductsPageLocators.FILTER_ZA_OPTION,
            "Price (low to high)": ProductsPageLocators.FILTER_LOW_HIGH_OPTION,
            "Price (high to low)": ProductsPageLocators.FILTER_HIGH_LOW_OPTION
        }
        browser.element(ProductsPageLocators.FILTER_DROPDOWN_MENU).click()
        browser.element(filter_map[filter_name]).click()
        return self

    def get_product_names(self):
        return [element.get(query.text) for element in browser.all(ProductsPageLocators.PRODUCT_TITLE)]

    def are_products_sorted_ascending(self):
        product_names = self.get_product_names()
        return product_names == sorted(product_names)

    def are_products_sorted_descending(self):
        product_names = self.get_product_names()
        return product_names == sorted(product_names, reverse=True)

    def get_product_prices(self):
        return [element.get(query.text) for element in browser.all(ProductsPageLocators.PRODUCT_PRICE)]

    def get_numeric_prices(self):
        prices = self.get_product_prices()
        return [float(price.replace('$', '')) for price in prices]

    def are_product_prices_sorted_ascending(self):
        product_prices = self.get_numeric_prices()
        return product_prices == sorted(product_prices)

    def are_product_prices_sorted_descending(self):
        product_prices = self.get_numeric_prices()
        return product_prices == sorted(product_prices, reverse=True)

    def should_have_cart_counter(self, value):
        browser.element(ProductsPageLocators.SHOPPING_CART_COUNTER).should(have.exact_text(str(value)))
        return self

    def should_not_have_cart_counter(self):
        browser.element(ProductsPageLocators.SHOPPING_CART_COUNTER).should(be.not_.visible)
        return self