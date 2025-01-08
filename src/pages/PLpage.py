from pytest_playwright.pytest_playwright import page

from src.pages.AddtoCard import AddtoCard
from src.pages.CheckOut import CheckOut
from src.pages.PdPage import PdPage


class PLpage:
    def __init__(self, page):
        self.page = page
        self._asserloc = page.get_by_text("Pre-Loved", exact=True)   #expect locator
        self._nextbtn = page.locator("//li[@class='page-item font-weight-bold page-next']/a")
        self._plproductloc = page.locator("//div[@class='productImage']/following-sibling::div[@class='card-body']/div[@class='caption']/div[text()='Apple MacBook Air 6,1 (A1465 Early 2013) Core i5 1.3GHz 11 inch, RAM 4GB, 128GB SSD 1.5GB VRAM, ENG KB - Silver']")
        self._wishlist_loc = page.locator("// div[text() = 'Genuine Apple magic keyboard  for Mac A2450 - Soft Pink']/ancestor::div[@class ='product-card style2ProductCard listing-products']//button[@title='Add to wishlist']")
        self._clickonwishlist= page.locator("//a[@class='topbar-link dropdown-toggle']/ancestor::div[@class='topbar-text dropdown disable-autohide']//div/a[@href='https://www.cartlow.com/user/wishlist']")
        self._hoveronaccount= page.locator("//a[@class='topbar-link dropdown-toggle']")
        self._whislistitemloc= page.locator("//div/a[text()='Genuine Apple magic keyboard  for Mac A2450 - Soft Pink']/ancestor::div[@class='pr-md-2']//div/a[1]")
        self._checkoutwhislistloc = page.locator("//a[text()='Checkout']")
        self._add_to_card_icon_loc = page.locator("//span[text()='Cart']")

    def expectedplpagelocator(self):
        return self._asserloc

    def clickonproductplp(self, product_title):
        self.page.locator(f"//div[@class='productImage']/following-sibling::div[@class='card-body']/div[@class='caption']/div[text()='{product_title}']").click()
        # self.page.wait_for_timeout(7000)
        return PdPage(self.page)

    def addtowhishlist(self):
        self._wishlist_loc.click()
        self.page.wait_for_timeout(4000)
        return self
    def hoveronaccount(self):
        self.page.locator("//a[@class='topbar-link dropdown-toggle']").hover()
        self._clickonwishlist.click()
        self.page.wait_for_timeout(1000)
        return self

    def wishlistitemaddtocard(self, product_title):
        self.page.locator(f"//div/a[text()='{product_title}']/ancestor::div[@class='pr-md-2']//div/a[1]").click()
        self.page.wait_for_timeout(1000)
        return self

    def whislistcheckout(self):
        if self._checkoutwhislistloc.is_visible():
            self._checkoutwhislistloc.click()
            return CheckOut(self.page)
        else:
            self._add_to_card_icon_loc.click()
            return AddtoCard(self.page)


