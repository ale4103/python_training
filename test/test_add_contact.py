# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="sdfdsf", lastname="sdfsdfsdfsd", address="fdfsfdsfsfsd", mobile="9797987987"))
    app.session.logout()