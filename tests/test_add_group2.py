# -*- coding: utf-8 -*-
from model.parameters import Group


def test_add_group2(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create_new_group(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
