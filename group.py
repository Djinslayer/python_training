

class Group:

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

class Contact:

    def __init__(self, firstname, middlename, lastname, nickname, tittle, company, address_company, home_phone,
                 mobile_phone, work_phone, fax, mail1, mail2, mail3, homepage, birthday_year, anniversary_year,
                 address2, phone2, notes):
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
        self.birthday_year = birthday_year
        self.anniversary_year = anniversary_year
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
