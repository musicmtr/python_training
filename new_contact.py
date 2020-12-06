# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class NewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_add_new(wd)
        self.fill_contact_info(wd)
        self.back_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def back_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def fill_contact_info(self, wd):
        # поля ФИО, НИК
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("testname")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("testmidl")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("testlas")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("testnicl")
        # добавление фото
        wd.find_element_by_name("photo").click()
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys(u"C:\\fakepath\\Снимок экрана от 2020-12-05 17-39-40.png")
        # работа, контактные данные
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("testtit")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("testcomp")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("testadd - asd;m / asd/ 12")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("+7(864)151-424-77")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+7(919)151-44-44")
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("6161")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("5616156")
        # соц сети контакты
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("test@mail.ru")
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("test2@gmail.com")
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("awd@mail.ru")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("wfwef@vk.ru")
        # даты, выпадающим списком
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("December")
        wd.find_element_by_xpath("//option[@value='December']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1992")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("June")
        wd.find_element_by_xpath("(//option[@value='June'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1995")
        # принадлежность к группе
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("asd")
        wd.find_element_by_xpath("(//option[@value='16'])[3]").click()
        # заполение вторичных полей
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("wefwefawaefgwaeg\nawegawegaweg\nwaeg")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("WEFWF3")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("wefawef")
        # сохраняем изменения
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_add_new(self, wd):
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
