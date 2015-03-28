# -*- coding: utf-8 -*-
from model.parameters import *


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="a",firstname="aaaaaa", middlename="mmmmmm",  nickname="aaaaaaaa", title="k", homepage="m", company="dd", address="dd")
    app.contact.create_new_contact(contact, Phones(mobile="ssss", fax="s", home="a", work="djd"), Emails(email2="aaaaa", email="dd", email3="dk"), Address(address2="address", phone2="phone", notes="notes"))
    assert len(old_contacts)+1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)