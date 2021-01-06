from model.contact import Contact


def test_delete_first_contact(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.open_add_new()
        app.contact.fill_form(
            Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", telhome="", telmob="", telwork="", fax="",
                    email="", mail2="", mail3="", homepage="", years1="", years2="",
                    address2="", phone2="", nots="", bday="-", aday="-", bmonth="-", amonth="-",
                    photo=None))
        app.contact.save_created()
    app.contact.delete_first_contact()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)

