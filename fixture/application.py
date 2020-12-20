from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.navigation import Navigation_Helper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.navigation = Navigation_Helper(self)

    def destroy(self):
        self.wd.quit()
