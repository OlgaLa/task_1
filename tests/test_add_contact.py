# -*- coding: utf-8 -*-
from model.parameters import *


def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create_new_contact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)


