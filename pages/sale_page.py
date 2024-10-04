from time import sleep

from pages.locators import sale_locators as loc
from pages.base_page import BasePage
from playwright.sync_api import expect
import allure


class SalePage(BasePage):

    page_url = '/sale.html'

    @allure.step('check_title')
    def check_title(self, text):
        self.find(loc.page_title_loc)
        expect(self.find(loc.page_title_loc)).to_have_text(text)

    @allure.step('check_product_count')
    def check_product_count(self):
        products = self.find(loc.products_loc)
        product_count = products.count()
        expected_count = product_count
        assert product_count == expected_count
        expect(products).to_have_count(expected_count)

    @allure.step('women_s_deals_element')
    def women_s_deals_element(self, text):
        self.find(loc.pands_loc)
        expect(self.find(loc.pands_loc)).to_have_text(text)

    @allure.step('mens_bargains_element')
    def mens_bargains_element(self, text):
        self.find(loc.mens_loc)
        expect(self.find(loc.mens_loc)).to_have_text(text)

