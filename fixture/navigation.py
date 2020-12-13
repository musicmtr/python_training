from selenium.webdriver.firefox.webdriver import WebDriver


class Navigation_Helper:

    def __init__(self, app):
        self.app = app
        self.wd = WebDriver()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def back_home_page(self):
        self.wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/edit.php")