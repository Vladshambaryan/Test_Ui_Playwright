import allure
from pages.locators import create_account_locators as locc
from pages.base_page import BasePage
from playwright.sync_api import expect


class CreateAccount(BasePage):

    page_url = '/customer/account/create/'

    @allure.step('fill_incorrect_data')
    def fill_incorrect_data(self,  first, last, email, password, conf_password):
        first_field = self.find(locc.first_loc)
        last_field = self.find(locc.last_loc)
        email_field = self.find(locc.email_loc)
        password_field = self.find(locc.password_loc)
        conf_password_field = self.find(locc.conf_password_loc)
        button = self.find(locc.button_loc)
        first_field.fill(first)
        last_field.fill(last)
        email_field.fill(email)
        password_field.fill(password)
        conf_password_field.fill(conf_password)
        button.click()

    @allure.step('check_error_message_first_name')
    def check_error_message_first_name(self, text):
        expect(self.page.locator(locc.error_loc)).to_have_text(text)

    @allure.step('check_error_message_last_name')
    def check_error_message_last_name(self, text):
        expect(self.page.locator(locc.error_ln_loc)).to_have_text(text)

    @allure.step('check_error_message_first_and_last_name')
    def check_error_message_first_and_last_name(self, text):
        self.find(locc.error_fn_ln_loc).wait_for(state='visible')
        expect(self.page.locator(locc.error_fn_ln_loc)).to_have_text(text)

    @allure.step('fill_incorrect_email')
    def fill_incorrect_email(self, email):
        email_field = self.find(locc.email_loc)
        email_field.fill(email)
        button = self.find(locc.button_loc)
        button.click()

    @allure.step('check_message_incorrect_email')
    def check_message_incorrect_email(self, text):
        self.page.wait_for_load_state('networkidle')
        expect(self.page.locator(locc.email_error_loc)).to_have_text(text)

    @allure.step('check_message_confirm_password')
    def check_message_confirm_password(self, text):
        self.find(locc.conf_password_error_loc).wait_for(state='visible')
        expect(self.page.locator(locc.conf_password_error_loc)).to_have_text(text)

    @allure.step('fill_weak_password')
    def fill_weak_password(self, password):
        self.find(locc.password_loc).wait_for(state='visible')
        password_field = self.find(locc.password_loc)
        password_field.fill(password)
        self.find(locc.conf_password_error_loc).click()

    @allure.step('check_message_weak_password')
    def check_message_weak_password(self, text):
        self.find(locc.password_message_weak_loc).wait_for(state='visible')
        expect(self.page.locator(locc.password_message_weak_loc)).to_have_text(text)

    @allure.step('fill_medium_password')
    def fill_medium_password(self, password):
        self.find(locc.password_loc).wait_for(state='visible')
        password_field = self.find(locc.password_loc)
        password_field.fill(password)
        self.find(locc.conf_password_error_loc).click()

    @allure.step('check_message_medium_password')
    def check_message_medium_password(self, text):
        self.find(locc.password_message_medium_loc).wait_for(state='visible')
        expect(self.page.locator(locc.password_message_medium_loc)).to_have_text(text)

    @allure.step('fill_strong_password')
    def fill_strong_password(self, password):
        self.find(locc.password_loc).wait_for(state='visible')
        password_field = self.find(locc.password_loc)
        password_field.fill(password)
        self.find(locc.conf_password_error_loc).click()

    @allure.step('check_message_strong_password')
    def check_message_strong_password(self, text):
        self.find(locc.password_message_strong_loc).wait_for(state='visible')
        expect(self.page.locator(locc.password_message_strong_loc)).to_have_text(text)
