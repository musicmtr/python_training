import os
from model.contact import Contact
import random


def test_edit_info(app,  db, check_ui):
    old_contact = db.get_contact_list()
    if len(db.get_contact_list()) == 0:
        app.contact.open_add_new()
        app.contact.fill_form(
            Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", telhome="", telmob="", telwork="", fax="",
                    email="", mail2="", mail3="", homepage="", years1="", years2="",
                    address2="", phone2="", nots="", bday="-", aday="-", bmonth="-", amonth="-",
                    photo=None))
        app.contact.save_created()
    app.contact.open_home_page()

    contact = Contact(firstname="restname", middlename="restmidl", lastname="restlas", nickname="rettnicl", title="resttit", company="restcomp",
                                  address="restadd - asd;m / asd/ 12", telhome="+7(666)151-424-77", telmob="+7(666)151-44-44", telwork="444", fax="44444",
                                  email="rest@mail.ru", mail2="rest2@gmail.com", mail3="reawd@mail.ru", homepage="rewef@vk.ru", years1="1990", years2="1998",
                                  address2="rerererer", phone2="REEER", nots="REREf", bday="10", aday="10", bmonth="April", amonth="July", photo=None)
    contact1 = random.choice(old_contact)
    app.contact.select_contact_by_id_for_edit(contact1.id)
    app.contact.fill_form(contact)
    app.contact.save_edit_info()
    new_contact = db.get_contact_list()
    assert len(old_contact) == len(new_contact)
#    old_contact.remove(contact1)
#    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),  key=Contact.id_or_max)

