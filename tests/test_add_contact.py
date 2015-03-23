# -*- coding: utf-8 -*-
from model.parameters import *


def test_add_contact(app):
    app.contact.create_new_contact(Contact(firstname="aaaaaa", middlename="mmmmmm", lastname="a", nickname="aaaaaaaa", title="k", homepage="m", company="dd", address="dd"), Phones(mobile="ssss", fax="s", home="a", work="djd"), Emails(email2="aaaaa", email="dd", email3="dk"), Address(address2="address", phone2="phone", notes="notes"))


