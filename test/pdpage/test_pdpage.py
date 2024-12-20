from playwright.sync_api import expect

from src.pages.LoginPage import LoginPage


def test_pdp_to_checkout(set_up_tear_down) -> None:
    page= set_up_tear_down
    credential = {'email': 'muhammad.akmal@cartlow.com', 'password': 'Mianjee!123'}
    loginpage = LoginPage(page)
    categoryname = "Clearance"
    product_title = 'Apple MacBook Air 6,1 (A1465 Early 2013) Core i5 1.3GHz 11 inch, RAM 4GB, 128GB SSD 1.5GB VRAM, ENG KB - Silver'
    checkoutpage = loginpage.dologin(credential)\
        .getcategory(categoryname)\
        .clickonproductplp(product_title)\
        .click_on_add_to_card_button_pdp_page()\
        .click_on_checkout_btn()
    expect(checkoutpage._checkoutasser).to_have_text("Payment method")


def test_pdp_card_checkout(set_up_tear_down) -> None:
    page= set_up_tear_down
    credential = {'email': 'muhammad.akmal@cartlow.com', 'password': 'Mianjee!123'}
    loginpage = LoginPage(page)
    categoryname = "Clearance"
    product_title = 'Apple MacBook Air 6,1 (A1465 Early 2013) Core i5 1.3GHz 11 inch, RAM 4GB, 128GB SSD 1.5GB VRAM, ENG KB - Silver'
    addtocardpage = loginpage.dologin(credential) \
        .getcategory(categoryname) \
        .clickonproductplp(product_title) \
        .click_on_add_to_card_button_pdp_page() \
        .click_on_add_to_card_icon()\
        .click_increase_quantity()\
        .click_on_checkout_btn_add_to_card_page()
    expect(addtocardpage._checkoutasser).to_have_text("Payment method")
