import self
from playwright.sync_api import expect

from src.pages.LoginPage import LoginPage


def test_plpage(set_up_tear_down) -> None:
    page = set_up_tear_down
    credential = {'email': 'muhammad.akmal@cartlow.com', 'password': 'Mianjee!123'}
    loginpage = LoginPage(page)
    categoryname= "Clearance"
    product_title= 'Apple MacBook Air 6,1 (A1465 Early 2013) Core i5 1.3GHz 11 inch, RAM 4GB, 128GB SSD 1.5GB VRAM, ENG KB - Silver'
    pdpage = loginpage.dologin(credential)\
        .getcategory(categoryname)\
        .clickonproductplp(product_title)
    if pdpage._pdpasserloc.is_visible() or pdpage._gotocardbtn.is_visible():
        print("On Product Description Page")
    else:
        print("Not on Product Description Page")


def test_PLPage_addtowhislist_gotowhislist_addtocard_checkout(set_up_tear_down) -> None:
    page = set_up_tear_down
    credential = {'email': 'muhammad.akmal@cartlow.com', 'password': 'Test!123'}
    loginpage = LoginPage(page)
    categoryname = "Clearance"
    product_title = 'Genuine Apple magic keyboard  for Mac A2450 - Soft Pink'
    checkoutpage = loginpage.dologin(credential) \
        .getcategory(categoryname) \
        .addtowhishlist() \
        .hoveronaccount() \
        .wishlistitemaddtocard(product_title) \
        .whislistcheckout()\
        .click_on_checkout_btn_add_to_card_page()
    expect(checkoutpage._checkoutasser).to_have_text("Payment method")

