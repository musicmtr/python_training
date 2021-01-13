from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.navigation.home_page()
        self.contact_cache = None

    def open_add_new(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("add new").click()

    def open_edit_form(self, index):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("Last name")) > 0):
            wd.find_element_by_xpath("//tr[position()=2]//img[@title='Edit']").click()
            #wd.find_element_by_xpath("//tr[position()=%s]//img[@title='Edit']".format(index)).click()
            #wd.find_element_by_xpath("//tr[position()={0}]//img[@title='Edit']".format(index)).click()

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, field_name):
        wd = self.app.wd
        self.open_edit_form()
        # fill group form
        self.fill_form(field_name)
        self.save_edit_info()
        self.open_home_page()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

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
        self.contact_cache = None

    def save_created(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.navigation.back_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        # select first group
        return len(wd.find_elements_by_name("selected[]"))

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("Last name")) > 0):
            wd.find_element_by_link_text("home").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            table_id = wd.find_element_by_id("maintable")
            rows = table_id.find_elements_by_tag_name("tr") # берем все строки таблицы
            for row in rows[1:]:
                # начинаем с второй строки
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                last_name = cells[1].text
                first_name = cells[2].text
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id,
                                                  telhome=all_phones[0], telmob=all_phones[1], telwork=all_phones[2], fax=all_phones[3]))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        telhome = wd.find_element_by_name("home").get_attribute("value")
        telmob = wd.find_element_by_name("mobile").get_attribute("value")
        telwork = wd.find_element_by_name("work").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       telhome=telhome, telmob=telmob, telwork=telwork, fax=fax)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        telhome = re.search("H: (.*)", text).group(1)
        telmob = re.search("M: (.*)", text).group(1)
        telwork = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contact(telhome=telhome, telmob=telmob, telwork=telwork, fax=fax)
