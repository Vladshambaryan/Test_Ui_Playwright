from time import sleep

from playwright.sync_api import expect
from pages.locators import product_locators as prod
from pages.base_page import BasePage
import allure


class AnaRunningShort(BasePage):

    page_url = '/ana-running-short.html'

    @allure.step('check_product_name')
    def check_product_name(self, text):
        expect(self.find(prod.product_name_loc)).to_have_text(text)

    @allure.step('check_product_price')
    def check_product_price(self, text):
        expect(self.find(prod.product_price_loc)).to_have_text(text)

    @allure.step('check_product_size')
    def check_product_size(self, text):
        size_28 = self.find(prod.size_28_loc)
        size_28.click()
        expect(self.find(prod.selected_loc)).to_have_text(text)

    @allure.step('check_product_size_')
    def check_product_size_(self, text):
        size_29 = self.find(prod.size_29_loc)
        size_29.click()
        expect(self.find(prod.selected_loc1)).to_have_text(text)

    @allure.step('check_product_color')
    def check_product_color(self, text):
        self.find(prod.available_colors_loc).wait_for(state='visible')
        expect(self.find(prod.available_colors_loc)).to_have_text(text)

    @allure.step('add_to_compare')
    def add_to_compare(self):
        self.page.evaluate("window.scrollBy(0, 200);")
        self.page.wait_for_load_state('networkidle')
        self.find(prod.compare_loc).click()

    @allure.step('check_compare_list')
    def check_compare_list(self, text):
        self.find(prod.comparision_list_loc).wait_for(state='visible')
        expect(self.find(prod.comparision_list_loc)).to_have_text(text)

    @allure.step('add_product_to_cart')
    def add_product_to_cart(self):
        size = self.find(prod.size_loc)
        size.click()
        color = self.find(prod.color_loc)
        color.click()
        add_cart = self.find(prod.add_to_cart_loc)
        add_cart.click()

    @allure.step('check_count')
    def check_count(self, text):
        count = self.find(prod.count_loc)
        count.click()
        self.find(prod.count_loc).wait_for(state='visible')
        expect(self.find(prod.count_loc)).to_have_text(text)

    @allure.step('check_product_in_cart')
    def check_product_in_cart(self, text):
        self.find(prod.item_in_cart_loc).wait_for(state='visible')
        expect(self.find(prod.item_in_cart_loc)).to_have_text(text)

    @allure.step('check_add_to_cart_with_out_selected_size_color')
    def check_add_to_cart_with_out_selected_size_color(self, text):
        add_cart = self.find(prod.add_to_cart_loc)
        add_cart.click()
        expect(self.find(prod.color_error_loc)).to_have_text(text)
        expect(self.find(prod.size_error_loc)).to_have_text(text)
