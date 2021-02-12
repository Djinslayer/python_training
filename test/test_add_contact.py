# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="Anonimus", middlename="Anonim", lastname="Anonomovich",
                            nickname="Anonim_nick", tittle="test", company="MTS", address_company="Kazan",
                            home_phone="+7999999999", mobile_phone="+7888888888", work_phone="+7562562562",
                            fax="+7235235689", mail1="email@mail1.ru", mail2="email@mail2.ru", mail3="email@mail3.ru",
                            homepage="qxl-ex.ru", birthday_year="1990", anniversary_year="2010", address2="Kazan 2",
                            phone2="Home", notes="Notes"))
        app.logout()


def test_add_empty_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="", middlename="", lastname="",
                                   nickname="", tittle="", company="", address_company="",
                                   home_phone="", mobile_phone="", work_phone="",
                                   fax="", mail1="", mail2="", mail3="",
                                   homepage="", birthday_year="", anniversary_year="", address2="",
                                   phone2="", notes=""))
        app.logout()