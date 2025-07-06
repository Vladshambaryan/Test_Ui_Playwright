import pytest


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_first_name(create_account_page, data):
    create_account_page.open()
    create_account_page.fill_incorrect_data(data)
    create_account_page.check_error_message_first_name('First Name is not valid!')


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_last_name(create_account_page):
    create_account_page.open()
    create_account_page.fill_incorrect_data('Elon', '``V', '123abc1236@gmail.com', '12345678mM+$VV', '12345678mM+$VV')
    create_account_page.check_error_message_last_name('Last Name is not valid!')


@pytest.mark.negative
@pytest.mark.regression
def test_create_account_incorrect_first_last_name(create_account_page):
    create_account_page.open()
    create_account_page.fill_incorrect_data('``V', '``V', '123abc1236@gmail.com', '12345678mM+$VV', '12345678mM+$VV')
    create_account_page.check_error_message_first_and_last_name('First Name is not valid! Last Name is not valid!')


@pytest.mark.negative
@pytest.mark.regression
def test_validation_confirm_password(create_account_page):
    create_account_page.open()
    create_account_page.fill_incorrect_data('Elon', 'Mask', '123abc1235@gmail.com', '12345678mM+$VV', '12345678mM+$Vv')
    create_account_page.check_message_confirm_password('Please enter the same value again.')


@pytest.mark.regression
def test_check_password_complexity(create_account_page):
    create_account_page.open()
    create_account_page.fill_incorrect_email('123abc123gmailcom')
    create_account_page.check_message_incorrect_email('Please enter a valid email address (Ex: johndoe@domain.com).')
    create_account_page.fill_weak_password('1236787')
    create_account_page.check_message_weak_password('Weak')
    create_account_page.fill_medium_password('12345678mM+$')
    create_account_page.check_message_medium_password('Medium')
    create_account_page.fill_strong_password('12345678mM+$VV')
    create_account_page.check_message_strong_password('Strong')
