# -*- coding: utf-8 -*-
import pytest
from model.parameters import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group2(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="test2", header="test2", footer="test2"))
    app.session.logout()


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
