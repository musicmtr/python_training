# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.session.home_page(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.home_page(username="admin", password="secret")
    app.group.modify_first_group(Group(header="new_header"))
    app.session.logout()

def test_modify_group_footer(app):
    app.session.home_page(username="admin", password="secret")
    app.group.modify_first_group(Group(footer="new_footer"))
    app.session.logout()
