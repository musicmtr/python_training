from model.group import Group
from model.contact import Contact
import random


def test_add_contact_in_some_group(app, orm, json_contact):
    contact_inf = json_contact
    #Если группы нет, то добавляем
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="newgr1"))
        app.contact.open_home_page()
    # Если нет контакта добавляем
    if len(orm.get_contact_list()) == 0:
        app.contact.open_add_new()
        app.contact.fill_form(contact_inf)
        app.contact.save_created()
        app.contact.open_home_page()
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    app.contact.add_contact_in_group_by_id(contact.id, group.id)
    list_contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in list_contacts_in_group

def test_add_contact_in_group(app, orm, json_contact):
    contact_inf = json_contact
    #Если группы нет, то добавляем
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="newgr1"))
        app.contact.open_home_page()
    # Если свободного контакта от группы нет или нет контакта
    if len(orm.get_free_contacts()) == 0:
        app.contact.open_add_new()
        app.contact.fill_form(contact_inf)
        app.contact.save_created()
        app.contact.open_home_page()
    # Берем свободный контакт
    contact = random.choice(orm.get_free_contacts())
    # Смотрим есть ли свободная группа для контакта, если нет создаем ищем свободную группу добавляем в нее контакт
    if len(orm.get_groups_not_in_contacts(contact)) == 0:
        app.group.create(Group(name="group_for_contact"))
        app.contact.open_home_page()
    group = random.choice(orm.get_groups_not_in_contact(contact.id))
    app.contact.add_contact_in_group_by_id(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)
