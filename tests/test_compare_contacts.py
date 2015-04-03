def test_compare_contacts(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page == contact_from_edit_page
    assert contact_from_home_page.all_phones_from_home_page == contact_from_edit_page.merge_phones()
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == contact_from_edit_page.merge_mails()

