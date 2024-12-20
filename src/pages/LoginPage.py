from src.pages.HomePage import HomePage


class LoginPage:
    def __init__(self, page):
        self.page = page
        self._loginwithgoogle=page.locator("//span[text()='Sign In']")
        self._googleclckfn = page.locator("//div[@class='socialLogin']//a[@title='Sign In with Google']")
        self._email = page.locator("//input[@type='email']")
        self._nxtbtn= page.locator("//button[@jsname='LgbsSe']/span[text()='Next']")
        self._password = page.get_by_label("Enter your password")
        self._accountloc=page.locator("//div[@class='topbar-text dropdown disable-autohide']/a/span[@class='text username-limit']")

    def dologin(self, credential):
        self._loginwithgoogle.click()
        self._googleclckfn.click()
        self._email.fill(credential['email'])
        self._nxtbtn.click()
        self.page.wait_for_timeout(500)
        self._password.fill(credential['password'])
        self.page.wait_for_timeout(500)
        self._nxtbtn.click()
        self.page.wait_for_timeout(2000)
        return HomePage(self.page)