__author__ = 'Властелин Вселенной'

from model.parameters import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
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
        self.come_back_to_group_page()

    def update_group(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()
        self.come_back_to_group_page()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.come_back_to_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.come_back_to_group_page()
        self.group_cache = None

    def select_group(self):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def come_back_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def click_edit_group(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_new_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.click_new_group()
        self.fill_group_fields(group)
        self.submit_group_creation()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, group):
        wd = self.app.wd
        self.select_group_by_index(index)
        self.click_edit_group()
        self.fill_group_fields(group)
        self.update_group()
        self.group_cache = None

    def modify_group_by_id(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(group.id)
        self.click_edit_group()
        self.fill_group_fields(group)
        self.update_group()
        self.group_cache = None

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id =id))
        return list(self.group_cache)