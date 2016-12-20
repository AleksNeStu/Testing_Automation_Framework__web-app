#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Checking the connection to the data base of web-app."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import mysql.connector
import pytest

from constants import db


@pytest.mark.smoke_tests
def test_add_contact():
    connection = mysql.connector.connect(
        host=db.DB_SERVER, database=db.DB_NAME, user=db.DB_USER,
        password=db.DB_PASSWORD)
    assert 1 == 1