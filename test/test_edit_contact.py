import os
from model.contact import Contact
import time


def test_edit_info(app):
    app.session.home_page(username="admin", password="secret")
    app.contact.edit_info()
    app.contact.fill_info(Contact(firstname="restname", middlename="restmidl", lastname="restlas", nickname="rettnicl", title="resttit", company="restcomp",
                                  address="restadd - asd;m / asd/ 12", telhome="+7(666)151-424-77", telmob="+7(666)151-44-44", telwork="444", fax="44444",
                                  email="rest@mail.ru", mail2="rest2@gmail.com", mail3="reawd@mail.ru", homepage="rewef@vk.ru", years1="1990", years2="1999",
                                  address2="rerererer", phone2="REEER", nots="REREf", bday="10", aday="10", bmonth="April", amonth="July", photo=os.path.dirname(os.getcwd()) + "/test_data/pik.jpeg", newgroup="[none]"))
    app.contact.save_edit_info()
    time.sleep(5)
    app.session.logout()
