from playwright.sync_api import expect

from src.pages.LoginPage import LoginPage


def test_add_to_card_checkout(set_up_tear_down) -> None:
    page= set_up_tear_down
    credential = {'email': 'muhammad.akmal@cartlow.com', 'password': 'Mianjee!123'}
    loginpage = LoginPage(page)
    categoryname = "Clearance"
    product_title = 'Apple MacBook Air 6,1 (A1465 Early 2013) Core i5 1.3GHz 11 inch, RAM 4GB, 128GB SSD 1.5GB VRAM, ENG KB - Silver'
    addtocardpage = loginpage.dologin(credential) \
        .getcategory(categoryname) \
        .clickonproductplp(product_title) \
        .click_on_add_to_card_button_pdp_page() \
        .click_on_add_to_card_icon()
    expect(addtocardpage._addtocardassertionloc).to_have_text("Shopping Cart")