
def test_delete_first_contact(app):
    app.contact.open_contact_page()
    app.contact.select_first_contact()
    app.contact.delete_first_contact()
