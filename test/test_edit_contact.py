# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="sdfdsf"))
    app.contact.edit_first_contact(Contact(firstname="Aewjkerh", lastname="fksdjl", address="jgri", mobile="9797985555"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)