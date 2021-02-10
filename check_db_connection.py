from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
import random

db = ORMFixture(host="localhost", name="addressbook", user="root", password="")
#
# try:
#     groups = random.choice(db.get_group_list())
#     l = db.get_contacts_not_in_group(groups)
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass #db.destroy()

try:
    groups = db.get_group_list()
    #groupid = random.choice(groups).id
    l = db.get_free_contacts(groups)
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()

# try:
#     l = len(db.get_group_list())
#
#     print("результат", l)
#
# finally:
#     pass #db.destroy()


