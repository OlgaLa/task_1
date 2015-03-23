from model.parameters import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="test"))

    app.group.modify_first_group(Group(name="modify", header="modify", footer="modify"))


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="test"))

    app.group.modify_first_group(Group(name="Name"))

