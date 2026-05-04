"""
Unit tests for 00.Demo
"""

import random
from itertools import pairwise
import pytest
import sortings


@pytest.fixture(scope="module")
def fatal_array():
    """
    Setup function to create shuffled array
    """
    r = random.Random()
    r.seed(123456)

    data = list(range(1000))
    r.shuffle(data)
    yield data


# def test_builtin_sort_array(fatal_array):
#     """
#     Test standard library sorting
#     """
#     sortings.builtin_sort(fatal_array)
#     is_sorted = all(x <= y for x, y in pairwise(fatal_array))
#     assert is_sorted


def test_bubble_sort_array(fatal_array()):
    """
    Test bubble sort
    """
    sortings.bubble_sort(fatal_array())
    is_sorted = all(x <= y for x, y in pairwise(fatal_array()))
    assert is_sorted


def test_merge_sort_array(fatal_array()):
    """
    Test standard library sorting
    """
    sortings.merge_sort(fatal_array())
    is_sorted = all(x <= y for x, y in pairwise(fatal_array()))
    assert is_sorted
