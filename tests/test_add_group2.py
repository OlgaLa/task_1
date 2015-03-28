# -*- coding: utf-8 -*-
from model.parameters import Group


def test_add_group2(app):
    old_groups = app.group.get_group_list()
    group = Group(name="test2", header="test2", footer="test2")
    app.group.create_new_group(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_empty_group(app):
#    old_groups = app.group.get_group_list
#    group = Group(name="", header="", footer="")
#    app.group.create_new_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups)+1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)