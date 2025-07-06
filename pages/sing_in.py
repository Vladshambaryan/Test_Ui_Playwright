import allure
from playwright.sync_api import expect
from pages.locators import sing_in_locators as loc
from pages.base_page import BasePage


class LoginPage(BasePage):

    page_url = '/customer/account/login'

    @allure.step('sing_in_click')
    def sing_in_click(self):
        sing = self.find(loc.sing_loc)
        sing.click()

    @allure.step('fill_login_form')
    def fill_login_form(self, login, password):
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        sing_btn = self.find(loc.sing_btn_loc)
        email_field.fill(login)
        password_field.fill(password)
        sing_btn.click()

    @allure.step('check_text_is_welcome')
    def check_text_is(self, text):
        welcome = self.find(loc.welcome_loc)
        self.find(loc.welcome_loc).wait_for(state='visible')
        print(welcome.text_content())
        expect(self.find(loc.welcome_loc)).to_have_text(text)

    @allure.step('Check if the error alert text is as expected')
    def check_error_text(self, text):
        self.find(loc.error_loc).wait_for(state='visible')
        error = self.find(loc.error_loc)
        print(error.text_content())
        expect(self.find(loc.error_loc)).to_have_text(text)

    def change_quantity(self):
        self.page.locator("#quantity").select_option("4")