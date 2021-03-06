import re
from random import randrange
from model.contact import Contact


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_view_page.telhome) == clear(contact_from_edit_page.telhome)
    assert clear(contact_from_view_page.telmob) == clear(contact_from_edit_page.telmob)
    assert clear(contact_from_view_page.telwork) == clear(contact_from_edit_page.telwork)
    assert clear(contact_from_view_page.phone2) == clear(contact_from_edit_page.phone2)


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
    #print(contact_from_home_page.firstname, type(contact_from_edit_page.firstname))

# мой вариант без
# def test_get_only_id(app, db):
#     all_id = db.get_only_id()
#     s = db.get_contact_list()
#     contact_from_db = db.get_all_info_contact_list()
#     contact_home_page = []
#     for i in range(len(all_id)):
#         contact_from_home_page = app.contact.get_contact_list()[i]
#         contact_home_page.append(contact_from_home_page)
#     assert sorted(clearid(contact_home_page), key=Contact.id_or_max) == sorted(clearid(contact_from_db),  key=Contact.id_or_max)


def test_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_all_info_contact_list(), key=Contact.id_or_max)
    index = len(contacts_from_home_page)
    for i in range(index):
        contact_from_home_page = contacts_from_home_page[i]
        contact_from_db = contacts_from_db[i]
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert clear(contact_from_home_page.all_mail) == merge_email_like_on_home_page(contact_from_db)
        assert clear(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.address == contact_from_db.address




def clear(s):
    return re.sub("[() -]", "", s)


#работает именно с этим
def clearid(s):
    return re.sub("[() -]", "",
                  str())


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
