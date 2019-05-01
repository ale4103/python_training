# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="sdfdsf"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    app.contact.select_contact_by_id(contact.id)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = db.get_group_list()
    selected_group = random.choice(group)
    old_list_of_contacts_in_group = len(db.get_contacts_in_group(selected_group))
    app.group.select_group_from_group_menu(selected_group.id)
    app.contact.add_contact_to_group_by_id()
    new_list_of_contacts_in_group = len(db.get_contacts_in_group(selected_group))
    assert old_list_of_contacts_in_group + 1 == new_list_of_contacts_in_group

# def test_add_contact_to_group(app):
#     if len(db.get_group_list()) == 0:
#         app.group.create(Group(name="test"))
#     groups = db.get_group_list()
#     index = randrange(len(groups))
#     group_id = groups[index].id
#     contact = Contact(firstname="firstname", lastname="lastname", address="address", group=group_id)
#     old_contacts = db.get_contacts_in_group(Group(id=group_id))
#     app.contact.create(contact)
#     new_contacts = db.get_contacts_in_group(Group(id=group_id))
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)