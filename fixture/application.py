from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHepler
from fixture.contact import ContactHepler

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(15)
        self.session = SessionHelper(self)
        self.group = GroupHepler(self)
        self.contact = ContactHepler(self)

    def open_home_page(self):
            wd = self.wd
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
