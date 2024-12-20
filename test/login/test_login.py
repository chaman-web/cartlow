import re
from playwright.sync_api import Page, expect

from src.pages.LoginPage import LoginPage


def test_login_google(set_up_tear_down) -> None:
    page = set_up_tear_down
    credential = {'email': 'muhammad.akmal@cartlow.com', 'password': 'Mianjee!123'}
    loginpage=LoginPage(page)
    loginpage.dologin(credential)
    expect(loginpage._accountloc).to_have_text("Account")


def test_get_category(set_up_tear_down) -> None:
    page = set_up_tear_down
    # Select all 'li > a' elements
    locator = page.locator("li > a").all_text_contents()
    count = locator.count()

    print(f"Total number of links: {count}")

    # If you want to print the text of each link
    for i in range(count):
        print(f"Link Text {i + 1}: {locator.nth(i).text_content()}")

    # all_texts.count()
    # # Print the text of each link
    # for text in all_texts:
    #     print(f"Link Text: {text}")  # Indent this line properly

