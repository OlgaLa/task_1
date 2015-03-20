__author__ = 'Властелин Вселенной'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def click_create_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("групи").click()

    def click_new_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_fields(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def submit_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
        self.open_group_page()

    def update_group(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.open_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.select_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_group_page()

    def select_group(self):
        wd = self.app.wd
        self.click_create_group()
        # select first group
        wd.find_element_by_name("selected[]").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def click_edit_group(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()