from playwright.async_api import expect

from src.pages.HomePage import HomePage
from src.pages.LoginPage import LoginPage


def test_homepage(set_up_tear_down) -> None:
    page = set_up_tear_down
    credential = {'email': 'muhammad.akmal@cartlow.com', 'password': 'Test!123'}
    loginpage = LoginPage(page)
    categoryname = "Clearance"
    plpage = loginpage.dologin(credential)\
        .getcategory(categoryname)
    assert plpage._asserloc.inner_text() == 'Pre-Loved'
