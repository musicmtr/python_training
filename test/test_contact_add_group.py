from model.group import Group
from model.contact import Contact
import random



def test_modify_group_name(app, db, json_contact, orm):
    contacts = json_contact
    list_connect = db.get_info_address_in_groups()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="newgr1"))
        app.group.create(Group(name="newgr2"))
        app.group.create(Group(name="newgr3"))
    if len(db.get_contact_list()) == 0:
        app.contact.open_add_new()
        app.contact.fill_form(contacts)
        app.contact.save_created()
        app.contact.open_home_page()
    list_contact = orm.get_contact_list()
    list_group = orm.get_group_list()
    contact = random.choice(list_contact)
    number = random.choice(range(len(list_group)))
    #print("\n","ГРУПП ИД", id, "\n")
    app.contact.select_contact_by_id(contact.id)
    app.contact.edit_group(number)
    new_list_connect = db.get_info_address_in_groups()
    assert len(list_connect) + 1 == len(new_list_connect)

#
# def test_del_contact_in_group(app, db, json_contact):
#     contacts = json_contact
#     app.contact.open_home_page()
# #если нет то создаем группы
#     if len(db.get_info_address_in_groups()) == 0:
#         if len(db.get_group_list()) == 0:
#             app.group.create(Group(name="newgr1"))
# #елси нет то создаем контакты
#         if len(db.get_contact_list()) == 0:
#             app.contact.open_add_new()
#             app.contact.fill_form(contacts)
#             app.contact.save_created()
#             app.contact.open_home_page()
#     list_contact = db.get_contact_list()
#     list_group = db.get_group_list()
#     contact = random.choice(list_contact)
#     nomber = random.choice(range(len(list_group)))
#     app.contact.select_contact_by_id(contact.id)
#     app.contact.edit_group(nomber)
#     list_connect = db.get_info_address_in_groups()
#     id = random.choice(db.get_only_id_connect())
#     app.contact.del_in_group(id)
#     new_list_connect = db.get_info_address_in_groups()
#     assert len(list_connect) - 1 == len(new_list_connect)
#
# def test_add_contact_in_group(app, db):
#     contact_list = ORMFixture.get_group_list()
#     print(contact_list)