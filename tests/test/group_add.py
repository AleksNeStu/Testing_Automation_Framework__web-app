#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Group add module"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import unittest
from tests.fixtures.application import Application


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        # wd.driver.switch_to.alert().text
        return True
    except:
        return False


class group_add_data(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(**self.app.login_data)
        self.app.create_group(self.app.group_data)
        self.app.logout()

    def test_add_group_empty(self):
        self.app.login(**self.app.login_data)
        self.app.create_group(self.app.group_data_empty)
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()