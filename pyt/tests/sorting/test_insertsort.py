import pytest

from tests.common import genereate_test_case

from sorting.insertsort import insertion_sort


@pytest.mark.parametrize("array_length", [1, 100])
def test_insertion_sort(array_length):
    case, expectation = genereate_test_case(array_length)
    assert insertion_sort(case) == expectation
