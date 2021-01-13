# -*- coding: utf-8 -*-
import os
from model.contact import Contact


def test_new_contact(app):

    old_contact = app.contact.get_contact_list()
    app.contact.open_add_new()
    contact = Contact(firstname="testname", middlename="testmidl", lastname="testlas", nickname="testnicl", title="testtit",
                company="testcomp",
                address="testadd - asd;m / asd/ 12", telhome="+7(864)151-424-77", telmob="+7(919)151-44-44",
                telwork="6161", fax="5616156",
                email="test@mail.ru", mail2="test2@gmail.com", mail3="awd@mail.ru", homepage="wfwef@vk.ru",
                years1="1992", years2="1995",
                address2="wefwefawaefgwaeg\nawegawegaweg\nwaeg", phone2="WEFWF3", nots="wefawef", bday="4", aday="4",
                bmonth="May", amonth="June", photo=None)
    app.contact.fill_form(contact)
    app.contact.save_created()
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_new_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.open_add_new()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                  address="", telhome="", telmob="", telwork="", fax="",
                                  email="", mail2="", mail3="", homepage="", years1="", years2="",
                                  address2="", phone2="", nots="", bday="-", aday="-", bmonth="-", amonth="-",
                                  photo=None)
    app.contact.fill_form(contact)
    app.contact.save_created()
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
