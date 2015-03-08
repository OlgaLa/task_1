__author__ = 'Властелин Вселенной'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group=GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def open_contact_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//div/div[4]/div/i/a[2]").click()

    def destroy(self):
         self.wd.quit()
