import pytest


@pytest.mark.regression
def test_test_product_properties(ana_running_short_page):
    ana_running_short_page.open()
    ana_running_short_page.check_product_name("Ana Running Short")
    ana_running_short_page.check_product_price("$40.00")
    ana_running_short_page.check_product_size("28")
    ana_running_short_page.check_product_size_("29")
    ana_running_short_page.check_product_color("Color")


@pytest.mark.regression
def test_clickable_elements_on_page(ana_running_short_page):
    ana_running_short_page.open()
    ana_running_short_page.add_to_compare()
    ana_running_short_page.check_compare_list('You added product Ana Running Short to the comparison list.')


@pytest.mark.regression
def test_add_to_cart(ana_running_short_page):
    ana_running_short_page.open()
    ana_running_short_page.add_product_to_cart()
    ana_running_short_page.check_count('1')
    ana_running_short_page.check_product_in_cart('Ana Running Short')


@pytest.mark.regression
def test_check_add_to_cart_with_out_selected_size_color(ana_running_short_page):
    ana_running_short_page.open()
    ana_running_short_page.check_add_to_cart_with_out_selected_size_color('This is a required field.')
