# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefex, maxlen):
    symbols = string.ascii_letters + string.digits + '''string.punctuation + ''' " "*10
    return prefex + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]

#testdata = [
#   Group(name=name, header=header, footer=footer)
#   for name in ["", random_string("name", 10)]
#   for header in ["", random_string("name", 10)]
#   for footer in ["", random_string("name", 10)]
#   ]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
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
