class ShoppingCartPageLocators:
    SHOPPING_PAGE_TITLE = '//div[@class="app_logo" and contains(text(), "Swag Labs")]'
    SHOPPING_CART_ICON = '[data-test="shopping-cart-link"]'
    SHOPPING_CART_COUNTER = '[data-test="shopping-cart-badge"]'
    BURGER_MENU_ICON = '[data-test="open-menu"]'
    CART_LIST = '[data-test="cart-list"]'
    CART_ITEM = '[data-test="inventory-item"]'
    CART_QUANTITY_LABEL = '[data-test="cart-quantity-label"]'
    CART_DESC_LABEL = '[data-test="cart-quantity-label"]'

    PRODUCT_TITLE = '[data-test="inventory-item-name"]'
    PRODUCT_PRICE = '[data-test="inventory-item-price"]'
    PRODUCT_DESCRIPTION = '[data-test="inventory-item-desc"]'
    PRODUCT_QUANTITY = '[data-test="item-quantity"]'
    REMOVE_BUTTON = '[data-test^="remove-"]'

    CONTINUE_SHOPPING_BUTTON = '[data-test="continue-shopping"]'
    CHECKOUT_BUTTON = '[data-test="checkout"]'