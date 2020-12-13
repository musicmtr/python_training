# -*- coding: utf-8 -*-
import os
from model.contact import Contact
import time

def test_edit_info(app):
    app.session.login(username="admin", password="secret")
    time.sleep(5)
    app.contact.edit_info()
    time.sleep(5)
    app.contact.fill_info(Contact(firstname="testname", middlename="testmidl", lastname="testlas", nickname="testnicl", title="testtit", company="testcomp",
                                  address="testadd - asd;m / asd/ 12", telhome="+7(864)151-424-77", telmob="+7(919)151-44-44", telwork="6161", fax="5616156",
                                  email="test@mail.ru", mail2="test2@gmail.com", mail3="awd@mail.ru", homepage="wfwef@vk.ru", years1="1992", years2="1995",
                                  address2="wefwefawaefgwaeg\nawegawegaweg\nwaeg", phone2="WEFWF3", nots="wefawef", bday="4", aday="4", bmonth="May", amonth="June", photo=os.path.dirname(os.getcwd()) + "/test_data/pik.jpeg", newgroup="[none]"))
    time.sleep(5)
    app.contact.save_edit_info()
    time.sleep(5)
    app.session.logout()