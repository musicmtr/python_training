import re
from random import randrange


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
    assert contact_from_view_page.email == contact_from_edit_page.email
    assert contact_from_view_page.mail2 == contact_from_edit_page.mail2
    assert contact_from_view_page.mail3 == contact_from_edit_page.mail3


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
        map(lambda x: clear(x),
            filter(lambda x: x is not None,
                   [contact.telhome, contact.telmob, contact.telwork, contact.phone2]))))
