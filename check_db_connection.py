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
    groups = random.choice(db.get_contact_list())
    #print("TYPE GR", type(groups))
    #groupid = random.choice(groups)
    print("TIPE ID",type(groups))
    l = db.get_groups_not_in_contact((random.choice(db.get_contact_list()).id))
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


