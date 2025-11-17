class ProductsPageLocators:
    PAGE_TITLE = '.app_logo'
    BURGER_MENU_ICON = '[data-test="open-menu"]'
    SHOPPING_CART_ICON = '[data-test="shopping-cart-link"]'
    SHOPPING_CART_COUNTER = '[data-test="shopping-cart-badge"]'
    INVENTORY_LIST = '[data-test="inventory-list"]'

    FILTER_DROPDOWN_MENU = '[data-test="product-sort-container"]'
    FILTER_AZ_OPTION = '[value="az"]'
    FILTER_ZA_OPTION = '[value="za"]'
    FILTER_LOW_HIGH_OPTION = '[value="lohi"]'
    FILTER_HIGH_LOW_OPTION = '[value="hilo"]'

    # Generic locators for all items
    PRODUCT_ITEM = '[data-test="inventory-item"]'
    PRODUCT_TITLE = '[data-test="inventory-item-name"]'
    PRODUCT_PRICE = '[data-test="inventory-item-price"]'
    PRODUCT_DESCRIPTION = '[data-test="inventory-item-desc"]'
    ADD_TO_CART_BUTTON = '[data-test^="add-to-cart-"]'
    REMOVE_BUTTON = '[data-test^="remove-"]'
    PRODUCT_IMAGE = '.inventory_item_img'