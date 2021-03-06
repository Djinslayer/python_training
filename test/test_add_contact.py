# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + ' '*10
        return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#random_day = randint(1, 31)


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", tittle="", company="", address="",
                    home_phone="", mobile_phone="", work_phone="", fax="", mail1="", mail2="", mail3="",
                    homepage="", birthday_year="", anniversary_year="", address2="", phone2="", notes="")] + [
        Contact(firstname=random_string('firstname', 15), middlename=random_string('middlename', 20),
                lastname=random_string('lastname', 30), nickname=random_string('nickname', 30),
                tittle=random_string('tittle'), 20, company=random_string('company', 30),
                address=random_string('address', 30), home_phone=random_string('home_phone', 12),
                mobile_phone=random_string('mobile_phone', 12), work_phone=random_string('work_phone', 12),
                fax=random_string('fax', 12), mail1=random_string('mail1', 30), mail2=random_string('mail2', 30),
                mail3=random_string('mail3', 30), homepage=random_string('homepage', 30),
                bday='9', bmonth='November', birthday_year='1990', aday="20", amonth="April", anniversary_year="2010",
                address2=random_string('address2', 12), phone2=random_string('phone2', 12),
                notes=random_string('notes', 12), )
        for i in range(5)
]


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)