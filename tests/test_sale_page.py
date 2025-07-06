import pytest


@pytest.mark.regression
def test_sale_page(sale_page, data, name):
    sale_page.open()
    sale_page.check_title(data[name])
    sale_page.check_product_count()
    sale_page.women_s_deals_element('Pristine prices on pants, tanks and bras.')
    sale_page.mens_bargains_element('Stretch your budget with active attire')
