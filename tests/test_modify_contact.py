from model.parameters import *
from random import randrange


def test_modify_some_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_new_contact(Contact(firstname="1a", middlename="1", lastname="a", nickname="1", title="k", homepage="m", company="1", address="1"), Phones(mobile="1", fax="1", home="1", work="1"), Emails(email2="1", email="1", email3="1"), Address(address2="1", phone2="1", notes="1"))

    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="a", middlename="a", lastname="a", nickname="a", title="1", homepage="m", company="dd", address="dd")
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(contact, Phones(mobile="1", fax="1", home="1", work="1"), Emails(email2="1", email="1", email3="1"), Address(address2="1", phone2="1", notes="1"), index)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index]=contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

