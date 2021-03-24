import re
from random import randrange
from model.contact import Contact


def test_all_info_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Anonimus", middlename="Anonim", lastname="Anonomovich"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_email_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_all_info_on_home_page_and_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Anonimus", middlename="Anonim", lastname="Anonomovich"))
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address.strip(), mail1=contact.mail1.strip(), mail2=contact.mail2.strip(),
                       mail3=contact.mail3.strip(), home_phone=contact.home_phone.strip(),
                       mobile_phone=contact.mobile_phone.strip(), work_phone=contact.work_phone.strip(),
                       phone2=contact.phone2.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)


def clear(s):
    return re.sub('[() -]', '', s)

def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                                filter(lambda x: x is not None,
                                       [contact.mail1, contact.mail2, contact.mail3])))