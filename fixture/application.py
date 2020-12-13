from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def back_home_page(self):
        self.wd.find_element_by_link_text("home page").click()


    def fill_contact_info(self, contact):
        # поля ФИО, НИК
        self.wd.find_element_by_name("firstname").click()
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.firstname)
        self.wd.find_element_by_name("middlename").clear()
        self.wd.find_element_by_name("middlename").send_keys(contact.middlename)
        self.wd.find_element_by_name("lastname").clear()
        self.wd.find_element_by_name("lastname").send_keys(contact.lastname)
        self.wd.find_element_by_name("nickname").clear()
        self.wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # добавление фото
        if contact.photo is None:
            pass
        else:
            self.wd.find_element_by_name("photo").send_keys(contact.photo)
        # работа, контактные данные
        self.wd.find_element_by_name("title").click()
        self.wd.find_element_by_name("title").clear()
        self.wd.find_element_by_name("title").send_keys(contact.title)
        self.wd.find_element_by_name("company").clear()
        self.wd.find_element_by_name("company").send_keys(contact.company)
        self.wd.find_element_by_name("address").clear()
        self.wd.find_element_by_name("address").send_keys(contact.address)
        self.wd.find_element_by_name("home").click()
        self.wd.find_element_by_name("home").click()
        self.wd.find_element_by_name("home").clear()
        self.wd.find_element_by_name("home").send_keys(contact.telhome)
        self.wd.find_element_by_name("mobile").click()
        self.wd.find_element_by_name("mobile").clear()
        self.wd.find_element_by_name("mobile").send_keys(contact.telmob)
        self.wd.find_element_by_name("work").click()
        self.wd.find_element_by_name("work").clear()
        self.wd.find_element_by_name("work").send_keys(contact.telwork)
        self.wd.find_element_by_name("fax").clear()
        self.wd.find_element_by_name("fax").send_keys(contact.fax)
        # соц сети контакты
        self.wd.find_element_by_name("email").click()
        self.wd.find_element_by_name("email").clear()
        self.wd.find_element_by_name("email").send_keys(contact.email)
        self.wd.find_element_by_name("email2").click()
        self.wd.find_element_by_name("email2").clear()
        self.wd.find_element_by_name("email2").send_keys(contact.mail2)
        self.wd.find_element_by_name("email3").click()
        self.wd.find_element_by_name("email3").clear()
        self.wd.find_element_by_name("email3").send_keys(contact.mail3)
        self.wd.find_element_by_name("homepage").click()
        self.wd.find_element_by_name("homepage").clear()
        self.wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # даты, выпадающим списком
        self.wd.find_element_by_name("bday").click()
        self.Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        self.wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        self.wd.find_element_by_name("byear").click()
        self.wd.find_element_by_name("byear").clear()
        self.wd.find_element_by_name("byear").send_keys(contact.years1)
        self.wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        self.wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        self.wd.find_element_by_name("ayear").click()
        self.wd.find_element_by_name("ayear").clear()
        self.wd.find_element_by_name("ayear").send_keys(contact.years2)
        # принадлежность к группе
        self.wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.newgroup)
        # заполение вторичных полей
        self.wd.find_element_by_name("address2").click()
        self.wd.find_element_by_name("address2").clear()
        self.wd.find_element_by_name("address2").send_keys(contact.address2)
        self.wd.find_element_by_name("phone2").click()
        self.wd.find_element_by_name("phone2").clear()
        self.wd.find_element_by_name("phone2").send_keys(contact.phone2)
        self.wd.find_element_by_name("notes").click()
        self.wd.find_element_by_name("notes").clear()
        self.wd.find_element_by_name("notes").send_keys(contact.nots)
        # сохраняем изменения
        self.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.back_home_page()

    def open_add_new(self):
        self.open_add_new()
        self.wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/edit.php")

    def login(self, username, password):
        self.open_home_page()
        self.wd.find_element_by_name("user").click()
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(username)
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_id("LoginForm").submit()

    def destroy(self):
        self.wd.quit()