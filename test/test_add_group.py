# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
        group = json_groups
        old_groups = app.group.get_group_list()
        app.group.open_create_form()
        app.group.fill_group(group)
        app.group.submit_create()
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
