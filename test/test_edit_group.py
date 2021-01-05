from model.group import Group


def test_edit_first_group(app):
    old_groups = app.group.get_group_list()
    app.group.open_edit_form_for_first()
    app.group.fill_group(Group(name="reewgr1", header="reewgr1hed", footer="rewe"))
    app.group.submit_edit()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

