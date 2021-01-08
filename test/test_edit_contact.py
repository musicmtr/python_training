import os
from model.contact import Contact
from random import randrange


def test_edit_info(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.open_add_new()
        app.contact.fill_form(
            Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", telhome="", telmob="", telwork="", fax="",
                    email="", mail2="", mail3="", homepage="", years1="", years2="",
                    address2="", phone2="", nots="", bday="-", aday="-", bmonth="-", amonth="-",
                    photo=None))
        app.contact.save_created()
    app.navigation.home_page()
    index = randrange(len(old_contact))
    contact = Contact(firstname="restname", middlename="restmidl", lastname="restlas", nickname="rettnicl", title="resttit", company="restcomp",
                                  address="restadd - asd;m / asd/ 12", telhome="+7(666)151-424-77", telmob="+7(666)151-44-44", telwork="444", fax="44444",
                                  email="rest@mail.ru", mail2="rest2@gmail.com", mail3="reawd@mail.ru", homepage="rewef@vk.ru", years1="1990", years2="1998",
                                  address2="rerererer", phone2="REEER", nots="REREf", bday="10", aday="10", bmonth="April", amonth="July", photo=None)
    contact.id = old_contact[index].id
    app.contact.open_contact_to_edit_by_index(index)
    app.contact.fill_form(contact)
    app.contact.save_edit_info()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

