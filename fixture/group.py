class GroupHelper():

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init groups creation
        wd.find_element_by_name("new").click()
        # fill group firm
        self.fill_group(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select 1st group
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("selected[]")
        # submit deletion
        wd.find_element_by_name("delete").click()
        wd.find_element_by_name("selected[]")
        self.return_to_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select 1st group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("edit").click()
        # fill group firm
        self.fill_group(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def fill_group(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()