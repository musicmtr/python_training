from model.group import Group
from model.contact import Contact
import random



def test_add_contact_in_group(app, db, json_contact, orm):
    contacts = json_contact
    list_connect = db.get_info_address_in_groups()
    print("лист контакт:", "\n", list_connect, type(list_connect))
    #проверка на наличие групп, если нет, создать
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="newgr1"))
        app.group.create(Group(name="newgr2"))
        app.group.create(Group(name="newgr3"))
        app.contact.open_home_page()
    #Проверка на наличие контактов, если нет, создать
    if len(orm.get_contact_list()) == 0:
        app.contact.open_add_new()
        app.contact.fill_form(contacts)
        app.contact.save_created()
        app.contact.open_home_page()
    #Собираем информацию о контактах и группах
    list_contact = orm.get_contact_list()
    list_group = orm.get_group_list()
    for contact in list_contact:
        if len(orm.get_groups_not_in_contact(contact)) > 0:
            list_empty_group = orm.get_groups_not_in_contact(contact)
            index = list_empty_group[0].id
            break
            return contact, index
        else:
            app.group.create(Group(name="newemoty_group1111"))
            list_empty_group = orm.get_groups_not_in_contact(contact)
            index = list_empty_group[0].id
            return index, contact
            break
    #выборка контакта для добавления
    app.contact.open_home_page()
    app.contact.select_contact_by_id(contact.id)
    #выборка группы и добавление
    app.contact.edit_group_id(index)
    new_list_connect = db.get_info_address_in_groups()
    assert len(list_connect) + 1 == len(new_list_connect)
