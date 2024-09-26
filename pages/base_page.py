from playwright.sync_api import Page
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('open page')
    def open(self):
        self.page.goto(f'{self.base_url}{self.page_url}')

    @allure.step('Find elements by locator')
    def find(self, locator):
        return self.page.locator(locator)
