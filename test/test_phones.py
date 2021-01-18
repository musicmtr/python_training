import re
from random import randrange
from model.contact import Contact

'''
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.telhome == contact_from_edit_page.telhome
    assert contact_from_view_page.telmob == contact_from_edit_page.telmob
    assert contact_from_view_page.telwork == contact_from_edit_page.telwork
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def test_on_home_page(app):
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert clear(contact_from_home_page.all_mail) == merge_email_like_on_home_page(contact_from_edit_page)
    assert clear(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address
'''


def get_all_id_contact_list(self):
    list = []
    cursor = self.connection.cursor()
    try:
        cursor.execute("select id from addressbook where deprecated='0000-00-00 00:00:00'")
        for row in cursor:
            (id) = row
            list.append(Contact(id=str(id)))
    finally:
        cursor.close()
    return list

print(list)

def test_all_info(app, db):
    old_contact = db.get_all_id_contact_list()
    contact_home = []
    contact_db = []
    print(contact_db, contact_home, old_contact)
    for i in old_contact:
        contact_from_home_page = app.contact.get_contact_list()[i]
        contact_home.append(contact_from_home_page)
        contact_from_edit_page = db.get_all_info_contact_list(i)
        contact_db.append(contact_from_edit_page)
    print(contact_db, contact_home)
#    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
#    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#    assert clear(contact_from_home_page.all_mail) == merge_email_like_on_home_page(contact_from_edit_page)
#    assert clear(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_home_page(contact_from_edit_page)
#    assert contact_from_home_page.address == contact_from_edit_page.address


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
        map(lambda x: clear(x),
            filter(lambda x: x is not None,
                   [contact.telhome, contact.telmob, contact.telwork, contact.phone2]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
        map(lambda x: clear(x),
            filter(lambda x: x is not None,
                   [contact.email, contact.mail2, contact.mail3]))))
