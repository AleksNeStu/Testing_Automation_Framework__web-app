#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for check sessions."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"


def test_check_session(app):
    """Check of the session actual status."""
    assert app.session.check_session() == True