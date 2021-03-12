from model.contact import Contact
import random
import string

constant = [
    Contact(firstname=('firstname'), middlename=('middlename'), lastname=('lastname'), nickname=('nickname'),
            tittle=('tittle'), company=('company'), address=('address'), home_phone=('home_phone'),
            mobile_phone=('mobile_phone'), work_phone=('work_phone'), fax=('fax'), mail1=('mail1'), mail2=('mail2'),
            mail3=('mail3'), homepage=('homepage'), bday='9', bmonth='November', birthday_year='1990',
            aday="20", amonth="April", anniversary_year="2010", address2=('address2'), phone2=('phone2'), notes=('notes')),
    Contact(firstname=('firstname1'), middlename=('middlename1'), lastname=('lastname1'), nickname=('nickname1'),
            tittle=('tittle1'), company=('company1'), address=('address1'), home_phone=('home_phone1'),
            mobile_phone=('mobile_phone1'), work_phone=('work_phone1'), fax=('fax1'), mail1=('mail11'), mail2=('mail21'),
            mail3=('mail31'), homepage=('homepage1'), bday='9', bmonth='November', birthday_year='1990',
            aday="20", amonth="April", anniversary_year="2010", address2=('address21'), phone2=('phone21'),
            notes=('notes1'))
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' ' * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", tittle="", company="", address="",
                    home_phone="", mobile_phone="", work_phone="", fax="", mail1="", mail2="", mail3="",
                    homepage="", birthday_year="", anniversary_year="", address2="", phone2="", notes="")] + [
               Contact(firstname=random_string('firstname', 15), middlename=random_string('middlename', 20),
                       lastname=random_string('lastname', 30), nickname=random_string('nickname', 30),
                       tittle=random_string('tittle', 20), company=random_string('company', 30),
                       address=random_string('address', 30), home_phone=random_string('home_phone', 12),
                       mobile_phone=random_string('mobile_phone', 12), work_phone=random_string('work_phone', 12),
                       fax=random_string('fax', 12), mail1=random_string('mail1', 30), mail2=random_string('mail2', 30),
                       mail3=random_string('mail3', 30), homepage=random_string('homepage', 30),
                       bday='9', bmonth='November', birthday_year='1990', aday="20", amonth="April",
                       anniversary_year="2010",
                       address2=random_string('address2', 12), phone2=random_string('phone2', 12),
                       notes=random_string('notes', 12))
               for i in range(5)
           ]

