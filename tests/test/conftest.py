#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Foobar.py: Description of what foobar does."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest
from tests.fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    fixture.check_fixture_valid()
    request.addfinalizer(fixture.destroy)
    return fixture