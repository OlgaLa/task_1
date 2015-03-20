# -*- coding: utf-8 -*-
from model.parameters import *


def test_add_contact(app):
    app.contact.click_add_new_contact()
    app.contact.add_new_contact(Contact(firstname="aaaaaa", middlename="mmmmmm", lastname="a", nickname="aaaaaaaa", title="k", homepage="m", company="dd", address="dd"))
    app.contact.enter_phone_numbers(Phones(mobile="ssss", fax="s", home="a", work="djd"))
    app.contact.enter_emails(Emails(email2="aaaaa", email="dd", email3="dk"))
    app.contact.enter_address(Address(address2="address", phone2="phone", notes="notes"))
    # app.contact.enter_value_dropdown()
    app.contact.click_enter_btn()
    app.contact.open_contact_page()

