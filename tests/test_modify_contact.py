from model.parameters import *


def test_modify_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_new_contact(Contact(firstname="1a", middlename="1", lastname="a", nickname="1", title="k", homepage="m", company="1", address="1"), Phones(mobile="1", fax="1", home="1", work="1"), Emails(email2="1", email="1", email3="1"), Address(address2="1", phone2="1", notes="1"))

    app.contact.modify_first_contact(Contact(firstname="1", middlename="1", lastname="1", nickname="1", title="1", homepage="1", company="1", address="1"), Phones(mobile="1", fax="1", home="1", work="1"), Emails(email2="1", email="1", email3="1"), Address(address2="1", phone2="1", notes="1"))


