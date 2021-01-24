from model.group import Group
from model.contact import Contact
import random
import time


def test_modify_group_name(app, db, json_contact):
    old_contact = db.get_contact_list()
    id_group = db.get_group_list()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="newgr1"))
        app.group.create(Group(name="newgr2"))
        app.group.create(Group(name="newgr3"))
    contact = random.choice(old_contact)
    id = random.choice(range(len(id_group)))
    #print("\n","ГРУПП ИД", id, "\n")
    app.contact.select_contact_by_id(contact.id)
    app.contact.edit_group(id)


    time.sleep(5)


'''
def test_modify_group_name(app, db, json_contact):
    old_contact = db.get_contact_list()
    id_group = db.get_group_list()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="newgr1"))
        app.group.create(Group(name="newgr2"))
        app.group.create(Group(name="newgr3"))
    contact = json_contact
    id = random.choice(id_group)
    old_contact = db.get_contact_list()
    app.contact.open_add_new()
    app.contact.fill_form(contact)
    # измнеение группЫ
    app.contact.fill_group(id.name)
    app.contact.save_created()
    new_contact = db.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
'''
