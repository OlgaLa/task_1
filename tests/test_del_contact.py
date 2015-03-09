
def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_contact_page()
    app.contact.select_first_contact()
    app.contact.delete_first_contact()
    app.session.logout()