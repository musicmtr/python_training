from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="localhost", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()

# try:
#     l = db.get_contacts_in_all_groups()
#
#     print("результат", l)
#
# finally:
#     pass #db.destroy()


