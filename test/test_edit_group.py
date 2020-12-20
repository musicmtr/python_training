from model.group import Group


def test_edit_first_group(app):
    app.session.home_page(username="admin", password="secret")
    app.group.open_edit_form_for_first()
    app.group.fill_group(Group(name="reewgr1", header="reewgr1hed", footer="rewe"))
    app.group.submit_edit()
    app.session.logout()