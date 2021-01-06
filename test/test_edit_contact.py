import os
from model.contact import Contact
import time


def test_edit_info(app):
    if app.contact.count() == 0:
        app.contact.open_add_new()
        app.contact.fill_form(
            Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", telhome="", telmob="", telwork="", fax="",
                    email="", mail2="", mail3="", homepage="", years1="", years2="",
                    address2="", phone2="", nots="", bday="-", aday="-", bmonth="-", amonth="-",
                    photo=None))
        app.contact.save_created()
    app.navigation.home_page()
    app.contact.open_edit_form()
    app.contact.fill_form(Contact(firstname="restname", middlename="restmidl", lastname="restlas", nickname="rettnicl", title="resttit", company="restcomp",
                                  address="restadd - asd;m / asd/ 12", telhome="+7(666)151-424-77", telmob="+7(666)151-44-44", telwork="444", fax="44444",
                                  email="rest@mail.ru", mail2="rest2@gmail.com", mail3="reawd@mail.ru", homepage="rewef@vk.ru", years1="1990", years2="1998",
                                  address2="rerererer", phone2="REEER", nots="REREf", bday="10", aday="10", bmonth="April", amonth="July", photo=None))
    app.contact.save_edit_info()

