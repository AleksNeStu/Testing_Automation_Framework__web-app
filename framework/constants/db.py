#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Data for work with web-app's data base MySQL."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from test import conftest
import os


# Data from config file
config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "../test/config.json")
config = conftest.load_json(config_file)

# Data base data
DB_SERVER = config["server_name"]
DB_NAME = config["db_name"]
DB_USER = config["db_username"]
DB_PASSWORD = config["db_password"]