from playwright.sync_api import BrowserContext
from pages.create_account_page import CreateAccount
from pages.sing_in import LoginPage
from pages.ana_running_short_page import AnaRunningShort
from pages.sale_page import SalePage
from pages.eco_friendly_page import EcoFriendly
import pytest


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    playwright.chromium.launch(headless=True)
    page = context.new_page()
    page.set_viewport_size({'width': 1900, 'height': 1020})
    # page.evaluate("document.body.style.zoom='0.7'")
    return page


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def login_page(page):
    return LoginPage(page)


@pytest.fixture()
def create_account_page(page):
    return CreateAccount(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendly(page)


@pytest.fixture()
def ana_running_short_page(page):
    return AnaRunningShort(page)
