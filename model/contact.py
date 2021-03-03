from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, tittle=None, company=None,
                 address_company=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None, mail1=None,
                 mail2=None, mail3=None, homepage=None, bday=None, bmonth=None, birthday_year=None, aday=None,
                 amonth=None, anniversary_year=None, address2=None, phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.tittle = tittle
        self.company = company
        self.address_company = address_company
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.mail1 = mail1
        self.mail2 = mail2
        self.mail3 = mail3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.birthday_year = birthday_year
        self.aday = aday
        self.amonth = amonth
        self.anniversary_year = anniversary_year
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize