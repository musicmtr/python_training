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

#отметить чекбокс по ид
    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_contact_by_id_for_edit(self, id):
        wd = self.app.wd
#        find_element_by_xpath("//a[@href]")
        #wd.find_element_by_xpath('a [@href="edit.php?id="%s"]' % id).click()
        #wd.find_element_by_xpath('//a[@href="edit.php?id="%s]' % id).click()
        wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' % id).click()

#удаление чекбокса по ид
    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        # select чек бокс по ид
        self.select_contact_by_id(id)
        # кнопка удаления
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
#        self.app.navigation.home_page()
        self.open_home_page()
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

    def click_link(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div/div[4]/div/i/a").click()

    def del_in_group(self, id):
        wd = self.app.wd
        #wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//form[@id='right']").click()
        Select(wd.find_element_by_xpath("//select[@name='group']")).select_by_value(str(id))
        wd.find_elements_by_name("selected[]")[0].click()
        wd.find_element_by_xpath("//input[@name='remove']").click()
        self.click_link()
        self.contact_cache = None

    def edit_group(self, index):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_index(index)
        wd.find_element_by_xpath("//input[@name='add']").click()
        self.click_link()
        self.contact_cache = None

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
                firstname = cells[2].text
                address = cells[3].text
                all_mail = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=last_name, id=id, address=address,
                                                  all_phones_from_home_page=all_phones, all_mail=all_mail))
        return list(self.contact_cache)
        self.groups_cache = None

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
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        mail2 = wd.find_element_by_name("email2").get_attribute("value")
        mail3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       telhome=telhome, telmob=telmob, telwork=telwork, phone2=phone2,
                       email=email, mail2=mail2, mail3=mail3, address=address
                       )

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        telhome = re.search("H: (.*)", text).group(1)
        telmob = re.search("M: (.*)", text).group(1)
        telwork = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        content = wd.find_element_by_id("content")
        emails = content.find_elements_by_tag_name("a")
        email = emails[0].text
        mail2 = emails[1].text
        mail3 = emails[2].text
        return Contact(telhome=telhome, telmob=telmob, telwork=telwork, phone2=phone2, email=email, mail2=mail2, mail3=mail3)

    # добавление к старому списку нового значения
    def merge(self, lst1, lst2):
        for i in lst2:
            if i not in lst1:
                lst1.append(i)
        return lst1
        self.groups_cache = None
