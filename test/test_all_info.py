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
    db_list = db.get_contact_list()
    assert len(ui_list) == len(db_list)
    ui_list_sorted = sorted(ui_list, key=Contact.id_or_max)
    db_list_sorted = sorted(db_list, key=Contact.id_or_max)
    for i in range(len(db_list)):
        assert merge_emails_like_on_home_page(db_list_sorted[i]) == ui_list_sorted[i].all_email_from_home_page
        assert merge_phones_like_on_home_page(db_list_sorted[i]) == ui_list_sorted[i].all_phones_from_home_page


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