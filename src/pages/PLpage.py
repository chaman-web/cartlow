from pytest_playwright.pytest_playwright import page
from src.pages.PdPage import PdPage


class PLpage:
    def __init__(self, page):
        self.page = page
        self._asserloc = page.get_by_text("Pre-Loved", exact=True)   #expect locator
        self._plproductloc = page.locator("//div[@class='productImage']/following-sibling::div[@class='card-body']/div[@class='caption']/div[text()='Apple MacBook Air 6,1 (A1465 Early 2013) Core i5 1.3GHz 11 inch, RAM 4GB, 128GB SSD 1.5GB VRAM, ENG KB - Silver']")

    def expectedplpagelocator(self):
        return self._asserloc

    def clickonproductplp(self, product_title):
        self.page.locator(f"//div[@class='productImage']/following-sibling::div[@class='card-body']/div[@class='caption']/div[text()='{product_title}']").click()
        self.page.wait_for_timeout(7000)
        return PdPage(self.page)

