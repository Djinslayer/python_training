from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Anonimus", middlename="Anonim", lastname="Anonomovich"))
    app.contact.modify_first_contact(Contact(firstname="Anonimus_mod", middlename="Anonim_mod",
                        lastname="Anonomovich_mod", nickname="Anonim_nick_mod", tittle="test_mod", company="MTS_mod",
                        address_company="Kazan_mod", home_phone="+7999999999_mod", mobile_phone="+7888888888_mod",
                        work_phone="+7562562562_mod", fax="+7235235689_mod", mail1="email@mail1.ru_mod",
                        mail2="email@mail2.ru_mod", mail3="email@mail3.ru_mod", homepage="qxl-ex.ru_mod",
                        birthday_year="2000", anniversary_year="2020", address2="Kazan 2_mod",
                        phone2="Home_mod", notes="Notes_mod"))


def test_modify_contact_fio(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Anonimus", middlename="Anonim", lastname="Anonomovich"))
    app.contact.modify_first_contact(Contact(firstname="Mod", middlename="Mod", lastname="Mod"))


def test_modify_contact_conpany(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Anonimus", middlename="Anonim", lastname="Anonomovich"))
    app.contact.modify_first_contact(Contact(company="Mod", address_company="Mod"))
