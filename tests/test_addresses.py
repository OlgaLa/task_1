def test_addresses_on_home_page(app):
    address_from_home_page = app.contact.get_contact_list()[0]
    address_from_edit_page = app.contact.get_address_from_edit_page(0)
    assert address_from_home_page.address == address_from_edit_page.address


