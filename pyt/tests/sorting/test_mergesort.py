import pytest

from tests.common import genereate_test_case

from sorting.mergesort import mergesort


@pytest.mark.parametrize("array_length", [1, 100, 10000, 1000000])
def test_mergesort(array_length):
    case, expectation = genereate_test_case(array_length)
    assert mergesort(case) == expectation
