from model.group import Group
from model.contact import Contact
import random


def test_del_contact_in_group(app, db, orm, json_contact):
    contacts = json_contact
    app.contact.open_home_page()
#если нет то создаем группы
    if len(db.get_info_address_in_groups()) == 0:
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="newgr1"))
            app.contact.open_home_page()
#елси нет то создаем контакты
        if len(orm.get_contact_list()) == 0:
            app.contact.open_add_new()
            app.contact.fill_form(contacts)
            app.contact.save_created()
            app.contact.open_home_page()
        #создаем связь контакт группа если ее нет
        list_contact = orm.get_contact_list()
        list_group = orm.get_group_list()
        contact = random.choice(list_contact)
        number = random.choice(range(len(list_group)))
        # выборка контакта для добавления
        app.contact.select_contact_by_id(contact.id)
        # выборка группы и добавление
        app.contact.edit_group(number)
    list_connect = db.get_info_address_in_groups()
    #Выбор случайной группы с контактом с последующим удалением контакта из группы
    random_group = random.choice(orm.get_group_list_have_contacts())
    app.contact.del_in_group(int(random_group.id))
    new_list_connect = db.get_info_address_in_groups()
    assert len(list_connect) - 1 == len(new_list_connect)
