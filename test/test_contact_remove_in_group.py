from model.group import Group
from model.contact import Contact
import random


def test_del_contact_in_group(app, db, orm, json_contact):
    contact_inf = json_contact
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="newgr1"))
        app.group.create(Group(name="newgr2"))
        app.contact.open_home_page()
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_list()) == 0:
        app.contact.open_add_new()
        app.contact.fill_form(contact_inf)
        app.contact.save_created()
        app.contact.open_home_page()
    if len(orm.get_group_list_have_contacts()) == 0:
        contacts = random.choice(orm.get_contacts_not_in_group(group))
        app.contact.select_contact_by_id(contacts.id)
        # выборка группы и добавление
        app.contact.edit_group_id(group.id)
    random_group = random.choice(orm.get_group_list_have_contacts())
    app.contact.del_in_group(int(random_group.id))
    contact = random.choice(orm.get_contacts_not_in_group(group))
    assert contact in orm.get_contacts_not_in_group(group)
