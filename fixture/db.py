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
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
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
            cursor.execute('select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, '
                           'work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth,'
                           'ayear, address2, phone2, notes from addressbook where deprecated="0000-00-00 00:00:00"')
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, tittle, company, address, home_phone, mobile_phone,
                 work_phone, fax, mail1, mail2, mail3, homepage, bday, bmonth, birthday_year, aday, amonth,
                 anniversary_year, address2, phone2, notes) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                                    tittle=tittle, company=company, address=address, home_phone=home_phone,
                                    mobile_phone=mobile_phone, work_phone=work_phone, fax=fax, mail1=mail1, mail2=mail2,
                                    mail3=mail3, homepage=homepage, bday=bday, bmonth=bmonth, birthday_year=birthday_year,
                                    aday=aday, amonth=amonth, anniversary_year=anniversary_year, address2=address2,
                                    phone2=phone2, notes=notes))
        finally:
            cursor.close()
        return list

    def get_contact_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                list.append(Group(id=str(group_id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()