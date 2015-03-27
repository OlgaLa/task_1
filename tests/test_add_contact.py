# -*- coding: utf-8 -*-
from model.parameters import *


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="aaaaaa", middlename="mmmmmm", lastname="a", nickname="aaaaaaaa", title="k", homepage="m", company="dd", address="dd")
    app.contact.create_new_contact(contact, Phones(mobile="ssss", fax="s", home="a", work="djd"), Emails(email2="aaaaa", email="dd", email3="dk"), Address(address2="address", phone2="phone", notes="notes"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)