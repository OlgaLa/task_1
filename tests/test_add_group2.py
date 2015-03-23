# -*- coding: utf-8 -*-
from model.parameters import Group


def test_add_group2(app):
    app.group.create_new_group(Group(name="test2", header="test2", footer="test2"))


def test_empty_group(app):
    app.group.create_new_group(Group(name="", header="", footer=""))