#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for data base."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

import pytest

from constants import messages
from model.group import Group

@pytest.mark.smoke_tests
def test_db_matches_ui_for_group_list(app, db):
    """Check matches of data base and UI data via groups page."""
    if app.group.count_of_groups_groups() == 0:
        app.group.create_group_groups(Group())
    db_groups = db.list_of_groups_db()
    ui_groups = app.group.list_of_groups_groups()
    assert (sorted(db_groups, key=Group.id_or_max) ==
            sorted(ui_groups, key=Group.id_or_max),
            messages.COMPARE_DB_VS_UI.format(db_groups, ui_groups))