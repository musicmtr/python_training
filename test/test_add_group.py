# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.open_create_form()
    app.group.fill_group(Group(name="newgr1", header="newgr1hed", footer="nwe"))
    app.group.submit_create()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.open_create_form()
    app.group.fill_group(Group(name="", header="", footer=""))
    app.group.submit_create()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
