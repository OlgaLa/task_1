from model.parameters import *

def test_delete_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.click_add_new_contact()
        app.contact.add_new_contact(Contact(firstname="aaaaaa", middlename="mmmmmm", lastname="a", nickname="aaaaaaaa", title="k", homepage="m", company="dd", address="dd"))
        app.contact.enter_phone_numbers(Phones(mobile="ssss", fax="s", home="a", work="djd"))
        app.contact.enter_emails(Emails(email2="aaaaa", email="dd", email3="dk"))
        app.contact.enter_address(Address(address2="address", phone2="phone", notes="notes"))
        app.contact.click_enter_btn()
        app.contact.open_contact_page()

    app.contact.open_contact_page()
    app.contact.select_first_contact()
    app.contact.delete_first_contact()
