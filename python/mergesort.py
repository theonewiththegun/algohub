from random import randint


def merge(left: list[int], right: list[int]) -> list[int]:
    l_i, r_i = 0, 0
    out = []
    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            out.append(left[l_i])
            l_i += 1
        else:
            out.append(right[r_i])
            r_i += 1

    if l_i < len(left):
        out.extend(left[l_i:])
    if r_i < len(right):
        out.extend(right[r_i:])

    return out


def mergesort(x: list[int]) -> list[int]:
    if len(x) <= 1:
        return x

    mid = len(x) // 2
    left = mergesort(x[:mid])
    right = mergesort(x[mid:])

    return merge(left, right)


def genereate_test_case(list_len: int) -> tuple[list[int], list[int]]:
    x = [randint(0, 100) for _ in range(list_len)]
    return x, sorted(x)


# ToDo move to pytest
if __name__ == "__main__":
    test_cases = [
        genereate_test_case(1),
        genereate_test_case(100),
        genereate_test_case(10000),
    ]
    for i, case in enumerate(test_cases):
        try:
            res = mergesort(case[0])
            assert res == case[1]
            print(
                f"PASS! Test # passed. Input: {case[0]}, expected: {case[1]}, got: {res}"
            )
        except BaseException:
            print(
                f"FAIL! Test #{i} did not pass. Input: {case[0]}, expected: {case[1]}, got: {res}"
            )
