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
    # Проверка

    contact = random.choice(orm.get_free_contacts())
    # Смотрим есть ли свободная группа для контакта, если нет создаем ищем свободную группу добавляем в нее контакт
    if len(orm.get_group_list()) == len(orm.get_groups_in_contact(contact.id)):
        app.group.create(Group(name="group_for_contact"))
        app.contact.open_home_page()
        group = orm.get_groups_not_in_contact(contact.id)
        app.contact.edit_group_id(group.id)
        app.contact.open_home_page()
    group = random.choice(orm.get_groups_not_in_contact(contact.id))
    app.contact.select_contact_by_id(contact.id)
    # выборка группы и добавление
    app.contact.edit_group_id(group.id)
    assert contact in orm.get_contacts_in_group(group)