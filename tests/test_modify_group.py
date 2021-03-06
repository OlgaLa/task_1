from model.parameters import Group
import random


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_new_group(Group(name="test"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "modify group"
    app.group.modify_group_by_id(group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




#def test_modify_first_group_name(app):
#    if app.group.count() == 0:
#        app.group.create_new_group(Group(name="test"))

#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name="Name"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups)-1 == len(new_groups)

