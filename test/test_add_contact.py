# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Anonimus", middlename="Anonim", lastname="Anonomovich",
                      nickname="Anonim_nick", tittle="test", company="MTS", address="Kazan",
                      home_phone="+7999999999", mobile_phone="+7888888888", work_phone="+7562562562",
                      fax="+7235235689", mail1="email@mail1.ru", mail2="email@mail2.ru", mail3="email@mail3.ru",
                      homepage="qxl-ex.ru", bday="9", bmonth="November", birthday_year="1990", aday="20",
                      amonth="April", anniversary_year="2010", address2="Kazan 2", phone2="Home", notes="Notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", middlename="", lastname="",
#                               nickname="", tittle="", company="", address_company="",
#                               home_phone="", mobile_phone="", work_phone="",
#                               fax="", mail1="", mail2="", mail3="",
#                               homepage="", birthday_year="", anniversary_year="", address2="",
#                               phone2="", notes="")
#    app.contact.create(contact)
#    assert len(old_contacts) + 1 == app.contact.count()
#    new_contact = app.contact.get_contact_list()
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
