# -*- coding: utf-8 -*-
from model.contact import Contact


def test_new_contact(app, json_contact, check_ui, db):
    contact = json_contact
    old_contact = db.get_contact_list()
    app.contact.open_add_new()
    app.contact.fill_form(contact)
    app.contact.save_created()
    new_contact = db.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
#    old_contact.append(contact)
#    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(db.get_contact_list(),  key=Contact.id_or_max)
