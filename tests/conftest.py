import os

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from dotenv import load_dotenv

from model.pages.login_page import LoginPage
from model.pages.products_page import ProductsPage
from model.pages.shopping_cart import ShoppingCartPage
from utils import attach


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def set_browser(request):
    browser_version=request.config.getoption('--browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login=os.getenv('LOGIN')
    password=os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

@pytest.fixture
def login_page(set_browser):
    return LoginPage()

@pytest.fixture
def products_page(set_browser):
    return ProductsPage()

@pytest.fixture
def shopping_cart_page(set_browser):
    return ShoppingCartPage()

@pytest.fixture
def logged_in_user(login_page):
    """Fixture to log in as standard_user"""
    login_page.open()
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.press_login_button()