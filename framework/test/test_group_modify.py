#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for modifying groups."""
__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

import pytest

from constants import messages
from model.group import Group


@pytest.mark.smoke_tests
def test_modify_some_group(
        app, generator_entities_GroupFactory_generate_create_mixed):
    """Check of a possibility to modify exist group used random attributes of
    new object 'new_group'.
    """
    new_group = generator_entities_GroupFactory_generate_create_mixed
    if app.group.count_of_groups_groups() == 0:
        app.group.create_group_groups(Group())
    first_groups = app.group.list_of_groups_groups()
    new_group.id = first_groups[0].id
    ind = randrange(len(first_groups))
    app.group.modify_group_groups(ind, new_group)
    assert len(first_groups) == app.group.count_of_groups_groups()
    actual_groups = app.group.list_of_groups_groups()
    expected_groups = first_groups[:ind] + [new_group] + first_groups[ind+1:]
    assert (sorted(expected_groups, key=Group.id_or_max) ==
            sorted(actual_groups, key=Group.id_or_max),
            messages.COMPARE_EXP_VS_GOT.format(expected_groups, actual_groups))