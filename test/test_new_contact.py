# -*- coding: utf-8 -*-
from model.contact import Contact


def test_new_contact(app, json_contact):
    contact = json_contact
    old_contact = app.contact.get_contact_list()
    app.contact.open_add_new()
    app.contact.fill_form(contact)
    app.contact.save_created()
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
