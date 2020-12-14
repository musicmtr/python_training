def test_delete_first_group(app):
    app.session.home_page(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
