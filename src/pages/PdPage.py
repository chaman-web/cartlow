import self
from pytest_playwright.pytest_playwright import page

from src.pages.AddtoCard import AddtoCard
from src.pages.CheckOut import CheckOut


class PdPage:
    def __init__(self, page):
        self.page = page
        self._pdpasserloc = page.locator("//div[@class='form-row']//button[text()='Add to Cart']")
        self._gotocardbtn = page.locator("//button[text()='Go to Cart']")
        self._btncheckout = page.locator("//a[text()='Checkout']")
        self._add_to_card_icon_loc=page.locator("//span[text()='Cart']")


    def click_on_add_to_card_button_pdp_page(self):
        self._pdpasserloc.click()
        return self

    def click_on_checkout_btn(self):
        self._btncheckout.click()
        self.page.wait_for_timeout(3000)
        return CheckOut(self.page)


    def click_on_add_to_card_icon(self):
        self._add_to_card_icon_loc.click()
        return AddtoCard(self.page)

    def pdp_page_assertion(self):
        # Check if either of the locators is visible
        if self._pdpasserloc.is_visible() or self._gotocardbtn.is_visible():
            print("On Product Description Page")
        else:
            print("Not on Product Description Page")

