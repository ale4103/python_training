# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="Aewjkerh", lastname="fksdjl", address="jgri", mobile="9797985555"))