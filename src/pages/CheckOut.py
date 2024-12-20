from pytest_playwright.pytest_playwright import page


class CheckOut:
    def __init__(self, page):
        self.page= page
        self._checkoutasser = page.locator("//div[text()='Payment method']")

