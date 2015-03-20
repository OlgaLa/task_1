from model.parameters import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.click_new_group()
        app.group.fill_group_fields(Group(name="test"))
        app.group.submit_group_creation()

    app.group.delete_first_group()

