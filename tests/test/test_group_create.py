#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for creating groups."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

import pytest

from tests.constants import messages
from tests.generator.entities_factory import GroupFactory
from tests.model.group import Group


test_data = GroupFactory.create() + GroupFactory.create_empty()

@pytest.mark.smoke_tests
@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_some_group(app, group):
    """Check of a possibility to create new random group via groups page."""
    first_groups = app.group.list_of_groups_groups()
    app.group.create_group_groups(group)
    assert len(first_groups) + 1 == app.group.count_of_groups_groups()
    actual_groups = app.group.list_of_groups_groups()
    group.id = actual_groups[-1].id
    expected_groups = first_groups + [group]
    assert (sorted(expected_groups, key=Group.id_or_max) ==
            sorted(actual_groups, key=Group.id_or_max),
            messages.COMPARE_EXP_VS_GOT.format(expected_groups, actual_groups))