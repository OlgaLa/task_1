# -*- coding: utf-8 -*-
from model.parameters import Group


def test_add_group2(app):
    app.group.click_create_group()
    app.group.click_new_group()
    app.group.fill_group_fields(Group(name="test2", header="test2", footer="test2"))
    app.group.submit_group_creation()



def test_empty_group(app):
    app.group.click_create_group()
    app.group.click_new_group()
    app.group.fill_group_fields(Group(name="", header="", footer=""))
    app.group.submit_group_creation()