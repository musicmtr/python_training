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
    contacts = orm.get_contact_list()
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
    if len(groups) == len(orm.get_group_list()):
        for group in groups:
            id_group = group.id
            while True:
                free_contact = orm.get_contacts_not_in_group(Group(id=id_group))
                free_group = orm.get_groups_not_in_contact((random.choice(orm.get_contact_list()).id))
                #db.get_groups_not_in_contact((random.choice(db.get_contact_list()).id))
                if len(free_contact):
                    print("\n","SOOOOOOOOOOOOOOOOOOOOO",free_contact[0], type(random.choice(free_contact)))
                    print("ASSAAAAAAAAAAAAAAA", ((random.choice(free_contact))))
                    print("GRPPPPPPPPPPPPPPP", free_group[0], type(random.choice(free_group)))
                    print("GRAATTTTTTTTTTTTA", ((random.choice(free_group))))
                   # print(free_group, "ВОООТ")
                    break
        groups = random.choice(free_group)
        print("Группа",groups)
        contact = random.choice(free_contact)
        print("Контакт",contact)
        #group = random.choice(groups)
        app.contact.add_contact_in_group_by_id(contact.id, group.id)
        contacts_in_group = orm.get_contacts_in_group(group)
        assert contact in contacts_in_group


