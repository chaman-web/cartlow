import re
from playwright.sync_api import Page, expect

from src.pages.LoginPage import LoginPage


def test_login_google(set_up_tear_down) -> None:
    page = set_up_tear_down
    credential = {'email': 'muhammad.akmal@cartlow.com', 'password': 'Mianjee!123'}
    loginpage=LoginPage(page)
    loginpage.dologin(credential)
    expect(loginpage._accountloc).to_have_text("Account")