"""Tests for the file-order <-> UI-order LUT round-trip in SingleFileTab."""
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def tab(qapp):
    from ac7renamer.singlefiletab import SingleFileTab

    return SingleFileTab(parent=MagicMock())


def test_luts_contain_the_same_elements(tab):
    assert set(tab.lut_in_file_order) == set(tab.lut_in_ui_order)
    assert len(tab.lut_in_file_order) == 12
    assert len(tab.lut_in_ui_order) == 12


@pytest.mark.parametrize("i", list(range(12)))
def test_file_to_ui_to_file_round_trip(tab, i):
    assert tab.ui_order_to_file_order(tab.file_order_to_ui_order(i)) == i


@pytest.mark.parametrize("i", list(range(12)))
def test_ui_to_file_to_ui_round_trip(tab, i):
    assert tab.file_order_to_ui_order(tab.ui_order_to_file_order(i)) == i
