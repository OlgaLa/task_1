from model.parameters import Group


def test_modify_first_group(app):
    app.group.select_group()
    app.group.click_edit_group()
    app.group.fill_group_fields(Group(name="modify", header="modify", footer="modify"))
    app.group.update_group()


def test_modify_first_group_name(app):
    app.group.select_group()
    app.group.click_edit_group()
    app.group.fill_group_fields(Group(name="Name"))
    app.group.update_group()

