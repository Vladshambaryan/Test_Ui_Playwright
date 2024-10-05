import pytest


@pytest.mark.regression
def test_sing_in_page(login_page):
    login_page.open()
    login_page.sing_in_click()
    login_page.fill_login_form('123abc1235@gmail.com', '12345678mM+$VV')
    login_page.check_text_is('Welcome, Elon Mask!')


@pytest.mark.negative
def test_sing_in_page_incorrect_password(login_page):
    login_page.open()
    login_page.sing_in_click()
    login_page.fill_login_form('123abc1235abc@gmai.com', 'm96')
    login_page.check_error_text(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.')
