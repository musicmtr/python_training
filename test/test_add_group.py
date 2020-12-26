# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):

    app.group.open_create_form()
    app.group.fill_group(Group(name="newgr1", header="newgr1hed", footer="nwe"))
    app.group.submit_create()

def test_add_empty_group(app):

    app.group.open_create_form()
    app.group.fill_group(Group(name="", header="", footer=""))
    app.group.submit_create()

