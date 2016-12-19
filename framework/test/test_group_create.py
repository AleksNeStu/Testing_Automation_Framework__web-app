#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for creating groups."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest

from constants import messages
from model.group import Group


@pytest.mark.smoke_tests
def test_add_some_group(
        app, generator_entities_GroupFactory_generate_create_mixed):
    """Check of a possibility to create new random group via groups page."""
    group = generator_entities_GroupFactory_generate_create_mixed
    first_groups = app.group.list_of_groups_groups()
    app.group.create_group_groups(group)
    assert len(first_groups) + 1 == app.group.count_of_groups_groups()
    actual_groups = app.group.list_of_groups_groups()
    group.id = actual_groups[-1].id
    expected_groups = first_groups + [group]
    assert (sorted(expected_groups, key=Group.id_or_max) ==
            sorted(actual_groups, key=Group.id_or_max),
            messages.COMPARE_EXP_VS_GOT.format(expected_groups, actual_groups))