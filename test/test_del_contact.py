from model.contact import Contact
from fixture.contact import ContactHelper
import random


def test_delete_first_contact(app, db, check_ui):
    old_contact = app.contact.get_contact_list()
    if len(db.get_contact_list()) == 0:
        app.contact.open_add_new()
        app.contact.fill_form(
            Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", telhome="", telmob="", telwork="", fax="",
                    email="", mail2="", mail3="", homepage="", years1="", years2="",
                    address2="", phone2="", nots="", bday="-", aday="-", bmonth="-", amonth="-",
                    photo=None))
        app.contact.save_created()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.id)
    new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
    old_contact.remove(contact)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),  key=Contact.id_or_max)
