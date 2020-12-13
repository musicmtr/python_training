from selenium.webdriver.support.select import Select


class ContactHelper:


    def __init__(self, app):
        self.app = app

    def fill_info(self, contact):
        # поля ФИО, НИК
        wd = self.app.wd
        self.app.wd.find_element_by_name("firstname").click()
        self.app.wd.find_element_by_name("firstname").clear()
        self.app.wd.find_element_by_name("firstname").send_keys(contact.firstname)
        self.app.wd.find_element_by_name("middlename").clear()
        self.app.wd.find_element_by_name("middlename").send_keys(contact.middlename)
        self.app.wd.find_element_by_name("lastname").clear()
        self.app.wd.find_element_by_name("lastname").send_keys(contact.lastname)
        self.app.wd.find_element_by_name("nickname").clear()
        self.app.wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # добавление фото
        if contact.photo is None:
            pass
        else:
            self.app.wd.find_element_by_name("photo").send_keys(contact.photo)
        # работа, контактные данные
        self.app.wd.find_element_by_name("title").click()
        self.app.wd.find_element_by_name("title").clear()
        self.app.wd.find_element_by_name("title").send_keys(contact.title)
        self.app.wd.find_element_by_name("company").clear()
        self.app.wd.find_element_by_name("company").send_keys(contact.company)
        self.app.wd.find_element_by_name("address").clear()
        self.app.wd.find_element_by_name("address").send_keys(contact.address)
        self.app.wd.find_element_by_name("home").click()
        self.app.wd.find_element_by_name("home").click()
        self.app.wd.find_element_by_name("home").clear()
        self.app.wd.find_element_by_name("home").send_keys(contact.telhome)
        self.app.wd.find_element_by_name("mobile").click()
        self.app.wd.find_element_by_name("mobile").clear()
        self.app.wd.find_element_by_name("mobile").send_keys(contact.telmob)
        self.app.wd.find_element_by_name("work").click()
        self.app.wd.find_element_by_name("work").clear()
        self.app.wd.find_element_by_name("work").send_keys(contact.telwork)
        self.app.wd.find_element_by_name("fax").clear()
        self.app.wd.find_element_by_name("fax").send_keys(contact.fax)
        # соц сети контакты
        self.app.wd.find_element_by_name("email").click()
        self.app.wd.find_element_by_name("email").clear()
        self.app.wd.find_element_by_name("email").send_keys(contact.email)
        self.app.wd.find_element_by_name("email2").click()
        self.app.wd.find_element_by_name("email2").clear()
        self.app.wd.find_element_by_name("email2").send_keys(contact.mail2)
        self.app.wd.find_element_by_name("email3").click()
        self.app.wd.find_element_by_name("email3").clear()
        self.app.wd.find_element_by_name("email3").send_keys(contact.mail3)
        self.app.wd.find_element_by_name("homepage").click()
        self.app.wd.find_element_by_name("homepage").clear()
        self.app.wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # даты, выпадающим списком
        self.app.wd.find_element_by_name("bday").click()
        Select(self.app.wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        self.app.wd.find_element_by_name("bmonth").click()
        Select(self.app.wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        self.app.wd.find_element_by_name("byear").click()
        self.app.wd.find_element_by_name("byear").clear()
        self.app.wd.find_element_by_name("byear").send_keys(contact.years1)
        self.app.wd.find_element_by_name("aday").click()
        Select(self.app.wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        self.app.wd.find_element_by_name("amonth").click()
        Select(self.app.wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        self.app.wd.find_element_by_name("ayear").click()
        self.app.wd.find_element_by_name("ayear").clear()
        self.app.wd.find_element_by_name("ayear").send_keys(contact.years2)
        # принадлежность к группе
        self.app.wd.find_element_by_name("new_group").click()
        Select(self.app.wd.find_element_by_name("new_group")).select_by_visible_text(contact.newgroup)
        # заполение вторичных полей
        self.app.wd.find_element_by_name("address2").click()
        self.app.wd.find_element_by_name("address2").clear()
        self.app.wd.find_element_by_name("address2").send_keys(contact.address2)
        self.app.wd.find_element_by_name("phone2").click()
        self.app.wd.find_element_by_name("phone2").clear()
        self.app.wd.find_element_by_name("phone2").send_keys(contact.phone2)
        self.app.wd.find_element_by_name("notes").click()
        self.app.wd.find_element_by_name("notes").clear()
        self.app.wd.find_element_by_name("notes").send_keys(contact.nots)
        # сохраняем изменения
        self.app.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.back_home_page()

    def open_add_new(self):
        wd = self.app.wd
        self.open_add_new()
        self.app.wd.find_element_by_link_text("add new").click()