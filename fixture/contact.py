class ContactHelper():

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def fill_contact(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        # wd.find_element_by_name("firstname").click()
        # wd.find_element_by_name("firstname").clear()
        # wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # wd.find_element_by_name("middlename").click()
        # wd.find_element_by_name("lastname").click()
        # wd.find_element_by_name("lastname").clear()
        # wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # wd.find_element_by_name("address").click()
        # wd.find_element_by_name("address").clear()
        # wd.find_element_by_name("address").send_keys(contact.address)
        # wd.find_element_by_name("mobile").click()
        # wd.find_element_by_name("mobile").clear()
        # wd.find_element_by_name("mobile").send_keys(contact.mobile)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))