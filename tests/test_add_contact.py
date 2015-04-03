# -*- coding: utf-8 -*-
from model.parameters import *
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation  +" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company='',
                      address='', homephone='', mobilephone='', workphone='', email2='', email='', email3='',
                      homepage='', address2='', secondaryphone='', notes='')] + [Contact(lastname=random_string("ln", 10), firstname=random_string("fn", 10),
             middlename=random_string("mn", 10), nickname=random_string("nn", 3),
             title=random_string("t", 10), company=random_string("co", 10), address=random_string("add", 10),
             mobilephone=random_string("mp", 10), homephone=random_string("hp", 10),
             workphone=random_string("wp", 10), email2=random_string("e2", 10),
             email=random_string("e", 10), email3=random_string("e3", 10), homepage=random_string("hp", 10),
             address2=random_string("add2", 20), secondaryphone=random_string("sph", 10), notes=random_string("notes", 10))
     for i in range (2)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contacts)+1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

