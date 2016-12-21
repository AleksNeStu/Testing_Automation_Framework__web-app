#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Data for work with web-app's data base MySQL."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import os

from test import conftest


# Data from config file
config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "../test/config.json")
config = conftest.load_json(config_file)


# IP address of the container with data base
db_server_ip_cmd = "docker inspect -f '{{range .NetworkSettings.Networks}}" \
                   "{{.IPAddress}}{{end}}' lamp_mariadb_1"
db_server_ip = conftest.get_bash_output(db_server_ip_cmd)

# Data base data
DB_SERVER = config["db_server"] if \
    db_server_ip == str(config["db_server"]) else db_server_ip
DB_NAME = config["db_name"]
DB_USER = config["db_username"]
DB_PASSWORD = config["db_password"]