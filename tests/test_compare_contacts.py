from model.parameters import Contact


def test_contact_compare(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_db)):
       assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname.strip()
       assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname.strip()
       assert contacts_from_home_page[i].address == contacts_from_db[i].address.strip()
       assert contacts_from_home_page[i].all_phones_from_home_page == contacts_from_db[i].merge_phones()
       assert contacts_from_home_page[i].all_emails_from_home_page == contacts_from_db[i].merge_emails()


#def test_compare_contacts(app):
#   contact_from_home_page = app.contact.get_contact_list()[0]
#   contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#   assert contact_from_home_page == contact_from_edit_page
#    assert contact_from_home_page.all_phones_from_home_page == contact_from_edit_page.merge_phones()
#    assert contact_from_home_page.address == contact_from_edit_page.address
#    assert contact_from_home_page.all_emails_from_home_page == contact_from_edit_page.merge_mails()





