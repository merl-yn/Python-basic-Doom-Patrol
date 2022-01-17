import pytest
import functions_for_testing as fp


def test_suma():
    assert fp.suma(4, 5) == 9
    assert fp.suma(12, 7) == 19
    assert fp.suma(119, 141) == 260


def test_dif():
    assert fp.dif(4, 5) == -1
    assert fp.dif(12, 7) == 5
    assert fp.dif(141, 119) == 22


def test_div():
    assert fp.div(9, 3) == 3
    assert fp.div(42, 21) == 2
    assert fp.div(684, 9) == 76


def test_multiple():
    assert fp.multiple(4, 5) == 20
    assert fp.multiple(12, 17) == 204
    assert fp.multiple(134, 284) == 38056
