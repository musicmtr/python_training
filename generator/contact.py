from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "test_data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefex, maxlen):
    symbols = string.ascii_letters + string.digits + '''string.punctuation + ''' " "*10
    return prefex + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                  address="", telhome="", telmob="", telwork="", fax="",
                                  email="", mail2="", mail3="", homepage="", years1="", years2="",
                                  address2="", phone2="", nots="", bday="-", aday="-", bmonth="-", amonth="-",
                                  photo=None)] + [
    Contact(firstname=random_string("name", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
        nickname=random_string("nickname", 10), title=random_string("title", 10), company=random_string("company", 10),
        address=random_string("address", 10), telhome=random_string("telhome", 10), telmob=random_string("telmob", 10),
        telwork=random_string("telwork", 5), fax=random_string("fax", 5), email=random_string("email", 10),
        mail2=random_string("mail2", 10), mail3=random_string("mail3", 10), homepage=random_string("homepage", 10),
        years1="1992", years2="1995", address2=random_string("address2", 10), phone2=random_string("phone2", 10),
        nots=random_string("nots", 10), bday="4", aday="4", bmonth="May", amonth="June", photo=None)
    for i in range(2)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
