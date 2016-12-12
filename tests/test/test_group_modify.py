#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Tests for modifying groups."""

__author__ = 'AleksNeStu'
__copyright__ = "The GNU General Public License v3.0"

from random import randrange

import pytest

from tests.constants import data, messages
from tests.generator.generic import random_data as r_data
from tests.model.group import Group


test_data = [Group(name=new_name, header=new_header, footer=new_footer)
             for new_name in ["", r_data(data.GROUP_NAME_NEW)]
             for new_header in ["", r_data(data.GROUP_HEADER_NEW)]
             for new_footer in ["", r_data(data.GROUP_FOOTER_NEW)]]

@pytest.mark.smoke_tests
@pytest.mark.parametrize("new_group", test_data,
                         ids=[repr(x) for x in test_data])
def test_modify_some_group(app, new_group):
    """Check of a possibility to modify exist group used random attributes of
    new object 'new_group'.
    """
    if app.group.count_of_groups_via_groups() == 0:
        app.group.create_group_via_groups(Group())
    first_groups = app.group.list_of_groups_via_groups()
    new_group.id = first_groups[0].id
    ind = randrange(len(first_groups))
    app.group.modify_group_via_groups(ind, new_group)
    assert len(first_groups) == app.group.count_of_groups_via_groups()
    actual_groups = app.group.list_of_groups_via_groups()
    expected_groups = first_groups[:ind] + [new_group] + first_groups[ind+1:]
    assert (sorted(expected_groups, key=Group.id_or_max) ==
            sorted(actual_groups, key=Group.id_or_max),
            messages.COMPARE_EXP_VS_GOT.format(expected_groups, actual_groups))