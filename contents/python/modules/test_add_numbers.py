
# pip install pytest
# import pytest
from add import add_numbers


def test_add_positive_numbers():
    assert add_numbers(3, 5) == 8


def test_add_negative_numbers():
    assert add_numbers(-3, -5) == -8


def test_add_mixed_numbers():
    assert add_numbers(3, -5) == -2
