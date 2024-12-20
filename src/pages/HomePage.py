from src.pages.PLpage import PLpage


class HomePage:
    def __init__(self,page):
        self.page = page
        self._linkcatloc=page.get_by_role("link", name="Clearance")

    def getcategory(self, categoryname):
        self.page.get_by_role(f"link", name=categoryname).click()
        return PLpage(self.page)

    # def clickoncategory(self, categoryname):
    #     self.getcategory(categoryname).click(timeout=5000)
    #     return self



