from model.group import Group


def test_edit_first_group(app):
    app.session.home_page(username="admin", password="secret")
    app.group.check_added()
    app.group.edit(Group(name="test_edit", header="tst_edit", footer="test_edit"))
    app.session.logout()
