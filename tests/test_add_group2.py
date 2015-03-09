# -*- coding: utf-8 -*-
from model.parameters import Group


def test_add_group2(app):
    app.session.login(username="admin", password="secret")
    app.group.click_create_group()
    app.group.click_new_group()
    app.group.create(Group(name="test2", header="test2", footer="test2"))
    app.group.submit_group_creation()
    app.session.logout()


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.click_create_group()
    app.group.click_new_group()
    app.group.create(Group(name="", header="", footer=""))
    app.group.submit_group_creation()
    app.session.logout()
