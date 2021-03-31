from model.contact import Contact
from random import randrange
import random
from fixture.orm import ORMFixture
from model.group import Group

def test_delete_contact_to_group(app, db):
    # проверка есть ли контакт
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(firstname="Anonimus_mod", middlename="Anonim_mod",
                    lastname="Anonomovich_mod", nickname="Anonim_nick_mod", tittle="test_mod", company="MTS_mod",
                    address="Kazan_mod", home_phone="+7999999999_mod", mobile_phone="+7888888888_mod",
                    work_phone="+7562562562_mod", fax="+7235235689_mod", mail1="email@mail1.ru_mod",
                    mail2="email@mail2.ru_mod", mail3="email@mail3.ru_mod", homepage="qxl-ex.ru_mod",
                    birthday_year="2000", anniversary_year="2020", address2="Kazan 2_mod",
                    phone2="Home_mod", notes="Notes_mod"))
    # проверка есть ли группа
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='name', header="header", footer="footer"))
    # проверка если ли контакты, добавленные в группу, если нет, то добавляем любой контакт в любую группу
    if len(db.get_contacts_in_groups_list()) == 0:
        contact = random.choice(db.get_contacts_not_in_any_group())
        group = random.choice(db.get_group_without_contacts())
        app.contact.add_contact_to_group_by_id(contact.id, group.name)
    contact = random.choice(db.get_contact_in_group())
    group = random.choice(db.get_group_with_contacts())
    old_contacts_in_group = db.get_contact_not_in_group()
    app.contact.delete_contact_from_group_by_id(contact.id, group.id)
    new_contacts_in_group = db.get_contact_not_in_group()
    assert len(new_contacts_in_group) - 1 == len(old_contacts_in_group)


