#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Contact add module"""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest
from tests.fixture.application import Application
from tests.generator.generic import random_data as r_data
from tests.generator.generic import random_email as r_email
from tests.model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name=r_data("name_", 5), email=r_email(5, "@gmail.com")))
    app.session.logout()


# def test_add_group_empty(app):
#     app.login(app.login_data)
#     app.create_group(app.group_data_empty)
#     app.logout()