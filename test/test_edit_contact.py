# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="sdfdsf"))
    app.contact.edit_first_contact(Contact(firstname="Aewjkerh", lastname="fksdjl", address="jgri", mobile="9797985555"))