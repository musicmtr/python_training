from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, telhome=None, telmob=None, telwork=None, fax=None, email=None, mail2=None, mail3=None, homepage=None, years1=None, years2=None, address2=None, phone2=None, nots=None,
                        bday=None, aday=None, bmonth=None, amonth=None, photo=None, all_phones_from_home_page = None, id=None):

        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.telhome = telhome
        self.telmob = telmob
        self.telwork = telwork
        self.fax = fax
        self.email = email
        self.mail2 = mail2
        self.mail3 = mail3
        self.homepage = homepage
        self.years1 = years1
        self.years2 = years2
        self.address2 = address2
        self.phone2 = phone2
        self.nots = nots
        self.bday = bday
        self.aday = aday
        self.bmonth = bmonth
        self.amonth = amonth
        self.photo = photo
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
