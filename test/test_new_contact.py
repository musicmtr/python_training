# -*- coding: utf-8 -*-
import os
from model.contact import Contact
import random
import string
import pytest


def random_string(prefex, maxlen):
    symbols = string.ascii_letters + string.digits + '''string.punctuation + ''' " "*10
    return prefex + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                  address="", telhome="", telmob="", telwork="", fax="",
                                  email="", mail2="", mail3="", homepage="", years1="", years2="",
                                  address2="", phone2="", nots="", bday="-", aday="-", bmonth="-", amonth="-",
                                  photo=None)] + [
    Contact(firstname=random_string("name", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
        nickname=random_string("nickname", 10), title=random_string("title", 10), company=random_string("company", 10),
        address=random_string("address", 10), telhome=random_string("telhome", 10), telmob=random_string("telmob", 10),
        telwork=random_string("telwork", 5), fax=random_string("fax", 5), email=random_string("email", 10),
        mail2=random_string("mail2", 10), mail3=random_string("mail3", 10), homepage=random_string("homepage", 10),
        years1="1992", years2="1995", address2=random_string("address2", 10), phone2=random_string("phone2", 10),
        nots=random_string("nots", 10), bday="4", aday="4", bmonth="May", amonth="June", photo=None)
    for i in range(2)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_new_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.open_add_new()
#    contact = Contact(firstname="testname", middlename="testmidl", lastname="testlas", nickname="testnicl", title="testtit",
#                company="testcomp",
#                address="testadd - asd;m / asd/ 12", telhome="+7(864)151-424-77", telmob="+7(919)151-44-44",
#                telwork="6161", fax="5616156",
#                email="test@mail.ru", mail2="test2@gmail.com", mail3="awd@mail.ru", homepage="wfwef@vk.ru",
#                years1="1992", years2="1995",
#                address2="wefwefawaefgwaeg\nawegawegaweg\nwaeg", phone2="WEFWF3", nots="wefawef", bday="4", aday="4",
#                bmonth="May", amonth="June", photo=None)
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
