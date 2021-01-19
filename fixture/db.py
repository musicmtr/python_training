import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_only_id(self):
        old_contact = self.get_contact_list()
        row = ''.join(str(e) for e in old_contact)
        idc = []
        # print(old_contact, idc,'\n', row)
        list_id = []
        id = ''
        for char in row:
            if char.isdigit():
                id = id + char
            else:
                if id != '':
                    list_id.append(int(id))
                    id = ''
        if id != '':
            idc.append(int(id))
        return list_id

    def get_all_info_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, telhome, telmob, telwork, phone2, email, mail2, mail3
                 ) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, telhome=telhome,
                                    telmob=telmob, telwork=telwork, phone2=phone2, email=email,
                                    mail2=mail2, mail3=mail3,))

        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
