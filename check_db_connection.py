from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

db = ORMFixture(host="localhost", name="addressbook", user="root", password="")

try:
    #contact = random.choice(orm.get_free_contacts())
    l = db.get_groups_in_contacts(Contact(id="13"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()

# try:
#     l = db.get_free_contacts()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass #db.destroy()

# try:
#     l = len(db.get_group_list())
#
#     print("результат", l)
#
# finally:
#     pass #db.destroy()


