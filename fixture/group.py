from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("group_page")) > 0):
            wd.find_element_by_link_text("group page").click()

    def open_edit_form_for_first(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("Edit+group") and len(wd.find_elements_by_name("Update")) > 0):
            self.open_groups_page()
            wd.find_element_by_name("selected[]").click()
            wd.find_element_by_name("edit").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def open_create_form(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("New+group") and len(wd.find_elements_by_name("group_page")) > 0):
            wd.find_element_by_link_text("groups").click()
            wd.find_element_by_name("new").click()

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group(self, group):
        wd = self.app.wd
        # заполнение данных групп
        self.change_field_value(field_name="group_name", text=group.name)
        self.change_field_value(field_name="group_header", text=group.header)
        self.change_field_value(field_name="group_footer", text=group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def submit_create(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def submit_edit(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def modify_first_group(self, new_group_date):
        wd = self.app.wd
        self.open_edit_form_for_first()
        # fill group form
        self.fill_group(new_group_date)
        self.submit_edit()
        self.return_to_groups_page()
        self.groups_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.open_create_form()
        self.fill_group(group)
        self.submit_create()
        self.groups_cache = None

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.groups_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.groups_cache.append(Group(name=text, id=id))

        return list(self.groups_cache)


