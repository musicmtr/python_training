from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.navigation.home_page()

    def open_add_new(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("add new").click()

    def open_edit_form(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("Last name")) > 0):
            wd.find_element_by_xpath("//tr[position()=2]//img[@title='Edit']").click()

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_form(self, contact):
        # поля ФИО, НИК
        wd = self.app.wd
        self.change_field_value(field_name="firstname", text=contact.firstname)
        self.change_field_value(field_name="middlename", text=contact.middlename)
        self.change_field_value(field_name="lastname", text=contact.lastname)
        self.change_field_value(field_name="nickname", text=contact.nickname)
        self.change_field_value(field_name="title", text=contact.title)
        # добавление фото
        if contact.photo is None:
            pass
        else:
            wd.find_element_by_name("photo").send_keys(contact.photo)
        # работа, контактные данные
        self.change_field_value(field_name="company", text=contact.company)
        self.change_field_value(field_name="address", text=contact.address)
        self.change_field_value(field_name="home", text=contact.telhome)
        self.change_field_value(field_name="mobile", text=contact.telmob)
        self.change_field_value(field_name="work", text=contact.telwork)
        self.change_field_value(field_name="fax", text=contact.fax)
        # соц сети контакты
        self.change_field_value(field_name="email", text=contact.email)
        self.change_field_value(field_name="email2", text=contact.mail2)
        self.change_field_value(field_name="email3", text=contact.mail3)
        self.change_field_value(field_name="homepage", text=contact.homepage)
        # даты, выпадающим списком
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        self.change_field_value(field_name="byear", text=contact.years1)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        self.change_field_value(field_name="ayear", text=contact.years2)
        self.change_field_value(field_name="address2", text=contact.address2)
        self.change_field_value(field_name="phone2", text=contact.phone2)
        self.change_field_value(field_name="notes", text=contact.nots)

    def save_edit_info(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.navigation.back_home_page()

    def save_created(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.navigation.back_home_page()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        # select first group
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("Last name")) > 0):
            wd.find_element_by_link_text("home").click()

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        table_id = wd.find_element_by_id("maintable")
        rows = table_id.find_elements_by_tag_name("tr") # берем все строки таблицы
        for row in rows[1:]:
            # начинаем с второй строки
            id = row.find_elements_by_tag_name("td")[0].get_attribute("value")
            last_name = row.find_elements_by_tag_name("td")[1].text
            first_name = row.find_elements_by_tag_name("td")[2].text
            contacts.append(Contact(firstname=first_name, lastname=last_name,  id=id))
        return contacts
