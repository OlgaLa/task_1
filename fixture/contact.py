import re

from  model.parameters import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def enter_address(self, address):
        wd = self.app.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(address.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(address.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(address.notes)

    def enter_phone_numbers(self, phone):
        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(phone.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(phone.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(phone.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(phone.fax)

    def enter_emails(self, email):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email.email3)

    def enter_value_dropdown(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1988")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[7]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1988")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[7]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[7]").click()

    def add_new_contact(self, contacts):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacts.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contacts.address)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contacts.homepage)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contacts.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contacts.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contacts.workphone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contacts.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contacts.email3)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contacts.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contacts.secondaryphone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contacts.notes)

    def add_new_contact_short_version(self, contacts):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)

    def click_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("добави нов").click()

    def click_enter_btn(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        self.delete_contact()

    def delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def click_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def click_update_btn(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("id('search_count')")) > 0):
            wd.find_element_by_link_text("начало").click()

    def count_contacts(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def create_new_contact(self, contacts):
        wd = self.app.wd
        self.click_add_new_contact()
        self.add_new_contact(contacts)
        self.click_enter_btn()
        self.open_contact_page()
        self.contact_cache = None

    def create_new_contact_short(self, contacts):
        wd = self.app.wd
        self.click_add_new_contact()
        self.add_new_contact_short_version(contacts)
        self.click_enter_btn()
        self.open_contact_page()
        self.contact_cache = None

    def modify_first_contact(self,):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, contacts, phone, email, address, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        self.click_edit_button()
        self.add_new_contact(contacts)
        self.enter_phone_numbers(phone)
        self.enter_emails(email)
        self.enter_address(address)
        self.click_update_btn()
        self.open_contact_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for row in wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = row.find_elements_by_css_selector('td')
                lastname = cells[1].text
                firstname = cells[2].text
                id = cells[0].find_element_by_css_selector('input').get_attribute('value')
                all_phones=cells[5].text
                address=cells[3].text
                all_emails=cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        self.click_edit_button()
        firstname =wd.find_element_by_name("firstname").get_attribute("value")
        lastname =wd.find_element_by_name("lastname").get_attribute("value")
        id =wd.find_element_by_name("id").get_attribute("value")
        homephone =wd.find_element_by_name("home").get_attribute("value")
        mobilephone =wd.find_element_by_name("mobile").get_attribute("value")
        workphone =wd.find_element_by_name("work").get_attribute("value")
        secondaryphone =wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                   homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                   address=address, email=email, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search('H: (.*)', text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()

    def select_contact_by_id_for_contact_to_group(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def add_contact_to_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='right']/select//option[1]").click()
        wd.find_element_by_name("add").click()

    def delete_contact_from_group(self):
        wd = self.app.wd
        wd.find_element_by_name("remove").click()

    def select_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@id='right']/select//option[3]").click()




