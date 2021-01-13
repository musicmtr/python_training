import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.telhome == clear(contact_from_edit_page.telhome)
    assert contact_from_home_page.telmob == clear(contact_from_edit_page.telmob)
    assert contact_from_home_page.telwork == clear(contact_from_edit_page.telwork)
    assert contact_from_home_page.fax == clear(contact_from_edit_page.fax)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.telhome == contact_from_edit_page.telhome
    assert contact_from_view_page.telmob == contact_from_edit_page.telmob
    assert contact_from_view_page.telwork == contact_from_edit_page.telwork
    assert contact_from_view_page.fax == contact_from_edit_page.fax

def clear(s):
    return re.sub("[() -]", "", s)
