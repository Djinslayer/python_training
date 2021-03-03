from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Anonimus", middlename="Anonim", lastname="Anonomovich"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

