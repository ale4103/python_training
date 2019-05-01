# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_delete_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="sdfdsf"))
    contacts = db.get_contact_list()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="wefwef"))
    groups = db.get_group_list()
    selected_group = random.choice(groups)
    list_of_contacts_in_group = db.get_contacts_in_group(selected_group)
    if len(list_of_contacts_in_group) == 0:
        contact = random.choice(contacts)
        app.contact.select_contact_by_id(contact.id)
        app.group.select_group_from_group_menu(selected_group.id)
        app.contact.add_contact_to_group_by_id()
        list_of_contacts_in_group = db.get_contacts_in_group(selected_group)
    count_contacts_in_group_before_deleting = len(db.get_contacts_in_group(selected_group))
    app.contact.open_group_page_with_contacts(selected_group.id)
    selected_contact = random.choice(list_of_contacts_in_group)
    app.contact.delete_contact_from_group_by_id(selected_contact.id)
    count_contacts_in_group_after_deleting = len(db.get_contacts_in_group(selected_group))
    assert count_contacts_in_group_before_deleting - 1 == count_contacts_in_group_after_deleting