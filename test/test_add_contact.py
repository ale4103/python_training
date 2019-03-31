# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(firstname="sdfdsf", lastname="sdfsdfsdfsd", address="fdfsfdsfsfsd", mobile="9797987987"))