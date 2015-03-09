from model.parameters import *


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_contact_page()
    app.contact.select_first_contact()
    app.contact.click_edit_button()
    app.contact.add_new_contact(Contact(firstname="1", middlename="1", lastname="1", nickname="1", title="1", homepage="1", company="1", address="1"))
    app.contact.enter_phone_numbers(Phones(mobile="1", fax="1", home="1", work="1"))
    app.contact.enter_emails(Emails(email2="1", email="1", email3="1"))
    app.contact.enter_address(Address(address2="1", phone2="1", notes="1"))
    app.contact.click_update_btn()
    app.contact.open_contact_page()
    app.session.logout()

