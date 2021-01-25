from model.group import Group
from model.contact import Contact
import random


# def test_modify_group_name(app, db, json_contact):
#     list_contact = db.get_contact_list()
#     list_group = db.get_group_list()
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="newgr1"))
#         app.group.create(Group(name="newgr2"))
#         app.group.create(Group(name="newgr3"))
#     contact = random.choice(list_contact)
#     nomber = random.choice(range(len(list_group)))
#     #print("\n","ГРУПП ИД", id, "\n")
#     app.contact.select_contact_by_id(contact.id)
#     app.contact.edit_group(nomber)

def test_del_contact_in_group(app, db):
    app.contact.open_home_page()
    if len(db.get_info_address_in_groups()) == 0:
        if len(db.get_group_list()) == 0:
            list_contact = db.get_contact_list()
            list_group = db.get_group_list()
            app.group.create(Group(name="newgr1"))
            contact = random.choice(list_contact)
            nomber = random.choice(range(len(list_group)))
            #print("\n","ГРУПП ИД", id, "\n")
            app.contact.select_contact_by_id(contact.id)
            app.contact.edit_group(nomber)
    all_connect = db.get_info_address_in_groups()
    name = random.choice(all_connect)
    id = random.choice(db.get_only_id_connect())

    app.contact.del_in_group(id)
    print(all_connect, "\n", name, "\n", id)
 #   print(type(name), type(list_name))

