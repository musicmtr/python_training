from model.group import Group
from model.contact import Contact
import random


def test_add_contact_in_some_group(app, orm, json_contact):
    contact_inf = json_contact
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="newgr1"))
        app.group.create(Group(name="newgr2"))
        app.group.create(Group(name="newgr3"))
        app.contact.open_home_page()
    group = random.choice(orm.get_group_list())

    if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.open_add_new()
        app.contact.fill_form(contact_inf)
        app.contact.save_created()
        app.contact.open_home_page()
    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.select_contact_by_id(contact.id)
    # выборка группы и добавление
    app.contact.edit_group_id(group.id)
    assert contact in orm.get_contacts_in_group(group)


