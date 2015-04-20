from model.parameters import *
from random import randrange


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="add", middlename="add", lastname="add", nickname="1", title="k", homepage="m", company="1", address="1"), Phones(mobile="1", fax="1", home="1", work="1"), Emails(email2="1", email="1", email3="1"), Address(address2="1", phone2="1", notes="1"))

    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="modify", middlename="a", lastname="modify", nickname="a", title="1", homepage="m", company="dd", address="dd")
    contact.id=old_contacts[index].id
    app.contact.modify_contact_by_index(contact, Phones(mobile="1", fax="1", home="1", work="1"),
                                        Emails(email2="1", email="1", email3="1"),
                                        Address(address2="", phone2="1", notes="1"), index)
    new_contacts = db.get_contact_list()
    old_contacts[index]=contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

