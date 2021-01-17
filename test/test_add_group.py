# -*- coding: utf-8 -*-
from model.group import Group


#testdata = [
#   Group(name=name, header=header, footer=footer)
#   for name in ["", random_string("name", 10)]
#   for header in ["", random_string("name", 10)]
#   for footer in ["", random_string("name", 10)]
#   ]


def test_add_group(app, json_groups):
        group = json_groups
        old_groups = app.group.get_group_list()
        app.group.open_create_form()
        #group = Group(name="newgr1", header="newgr1hed", footer="nwe")
        app.group.fill_group(group)
        app.group.submit_create()
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    app.group.open_create_form()
#    group = Group(name="", header="", footer="")
#    app.group.fill_group(group)
#    app.group.submit_create()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
