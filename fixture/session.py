class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password, base_url):
        wd = self.app.wd
        self.app.navigation.home_page(base_url=base_url)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def add_page(self, username, password):
        wd = self.app.wd
        self.app.navigation.open_edit_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("user")

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_loggin_in():
            self.logout()

    def is_loggin_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_loggin_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_loggin_in:
            if self.is_loggin_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

