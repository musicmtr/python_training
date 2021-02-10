from model.group import Group
from model.contact import Contact
import random


def test_add_contact_in_group2(app, orm, json_contact):
    contact_inf = json_contact
    #Если группы нет, то добавляем
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="newgr1"))
        app.contact.open_home_page()
    #Есть ли контакты
    if len(orm.get_contact_list()) == 0:
        app.contact.open_add_new()
        app.contact.fill_form(contact_inf)
        app.contact.save_created()
        app.contact.open_home_page()
    # заняты ли связи если да создадим группу, добавим существующий контакт в созданную группу
    groups = orm.get_group_list()
    if orm.all_contacts_in_all_groups(groups):
        app.group.create(Group(name="newgr1"))
        app.contact.open_home_page()
        contacts = orm.get_contact_list()
        groups = orm.get_free_group()
        contact = random.choice(contacts)
        group = random.choice(groups)
        app.contact.add_contact_in_group_by_id(contact.id, group.id)
        contacts_in_group = orm.get_contacts_in_group(group)
        assert contact in contacts_in_group
    # Ищу свободные паррые контакт группа
    if len(groups) == len(orm.get_group_list()):
        for group in groups:
            id_group = group.id
            while True:
                free_contact = orm.get_contacts_not_in_group(Group(id=id_group))
                free_group = orm.get_groups_not_in_contact((random.choice(orm.get_contact_list()).id))
                if len(free_contact):
                    break
        #Беру свободный контакта и для него создаю связь со случайной группой
        groups = random.choice(free_group)
        contact = random.choice(free_contact)
        app.contact.add_contact_in_group_by_id(contact.id, groups.id)
        contacts_in_group = orm.get_contacts_in_group(groups)
        assert contact in contacts_in_group


