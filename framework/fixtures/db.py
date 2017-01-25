#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Fixture for working with data base."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import mysql.connector
from model.group import Group

class DbFixture():
    """Class helper for work with data base."""
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(
            host=host, database=database, user=user, password=password)

    def list_of_groups_db(self):
        """Get list of groups objects via db."""
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, "
                           "group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header,
                                  footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        """Destroy connection with db."""
        self.connection.close()

