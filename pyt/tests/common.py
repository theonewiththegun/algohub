from random import randint


def genereate_test_case(list_len: int) -> tuple[list[int], list[int]]:
    x = [randint(0, 100) for _ in range(list_len)]
    return x, sorted(x)
