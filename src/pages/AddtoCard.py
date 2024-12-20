from src.pages.CheckOut import CheckOut


class AddtoCard:
    def __init__(self, page):
        self.page= page
        self._addtocardassertionloc = page.locator("//h2[text()='Shopping Cart']")
        self._quantityincrease = page.locator("//div[@class='cart-price-text']//div[@class='input-group']//input[@class='503635-button-plus button-plus']")
        self._addtocardcheckoutbtnloc = page.locator("//div[@class='card']/a[text()='Checkout']")

    def click_increase_quantity(self):
        self._quantityincrease.click()
        return self

    def click_on_checkout_btn_add_to_card_page(self):
        self._addtocardcheckoutbtnloc.click()
        return CheckOut(self.page)