from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Anonimus", middlename="Anonim", lastname="Anonomovich"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

