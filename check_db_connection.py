from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

db = ORMFixture(host="localhost", name="addressbook", user="root", password="")

try:
    l = db.get_groups_not_in_contact(Contact(id="66"))
    # for item in l:
    #     print(item)
    print(l)
finally:
    pass #db.destroy()

# try:
#     l = db.get_contacts_in_all_groups()
#
#     print("результат", l)
#
# finally:
#     pass #db.destroy()


