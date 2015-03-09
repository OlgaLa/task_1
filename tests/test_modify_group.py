from model.parameters import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.select_group()
    app.group.click_edit_group()
    app.group.create(Group(name="modify", header="modify", footer="modify"))
    app.group.update_group()
    app.session.logout()
