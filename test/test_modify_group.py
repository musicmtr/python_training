# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="newgr1"))
    app.group.modify_first_group(Group(name="New group2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(header="hea"))
    app.group.modify_first_group(Group(header="new_header2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_footer(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(footer="fooo"))
    app.group.modify_first_group(Group(footer="new_footer2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

