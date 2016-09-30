# -*- coding: utf-8 -*-

import unittest
from selenium.webdriver.firefox.webdriver import WebDriver
from tests.data.contact import Contact
from tests.generator.generic import random_data as r_data
from tests.generator.generic import random_email as r_email


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class contact_add_data(unittest.TestCase):

    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.login_data = {"username": "admin",
                           "password": "secret"}
        self.contact_data = Contact(name=r_data("name_", 5),
                                    email=r_email(5, "@gmail.com"))
        self.contact_data_empty = Contact(name="", email="")
    
    def test_add_contact(self):
        self.login(**self.login_data)
        self.create_contact(self.contact_data)
        self.logout()

    def test_add_contact_empty(self):
        self.login(**self.login_data)
        self.create_contact(self.contact_data_empty)
        self.logout()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://lamp/addressbook/index.php")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_contacts_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.wd
        self.open_contacts_page()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.name)
        wd.find_element_by_xpath("//div[@id='content']/form/input[2]").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()