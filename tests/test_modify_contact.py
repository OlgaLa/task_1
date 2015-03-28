from model.parameters import *


def test_modify_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_new_contact(Contact(firstname="1a", middlename="1", lastname="a", nickname="1", title="k", homepage="m", company="1", address="1"), Phones(mobile="1", fax="1", home="1", work="1"), Emails(email2="1", email="1", email3="1"), Address(address2="1", phone2="1", notes="1"))

    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="1", middlename="1", lastname="1", nickname="1", title="1", homepage="m", company="dd", address="dd")
    app.contact.modify_first_contact(contact, Phones(mobile="1", fax="1", home="1", work="1"), Emails(email2="1", email="1", email3="1"), Address(address2="1", phone2="1", notes="1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0]=contact
    assert old_contacts == new_contacts
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

