def merge(l: list[int], r: list[int]):
    l_i, r_i = 0, 0
    out = []
    while l_i < len(l) and r_i < len(r):
        if l[l_i] <= r[r_i]:
            out.append(l[l_i])
            l_i += 1
        else:
            out.append(r[r_i])
            r_i += 1

    if l_i < len(l):
        out.extend(l[l_i:])
    if r_i < len(r):
        out.extend(r[r_i:])

    return out


def mergesort(x: list[int]):
    if len(x) <= 1:
        return x

    mid = len(x) // 2
    l = mergesort(x[:mid])
    r = mergesort(x[mid:])

    return merge(l, r)


# ToDo move to pytest
if __name__ == "__main__":
    test_cases = [
        (list("9384756021"), list("0123456789")),
        ([1, 2, 4, 4, 6, 5, 3, 3, 3, 3], [1, 2, 3, 3, 3, 3, 4, 4, 5, 6]),
    ]
    for i, case in enumerate(test_cases):
        try:
            res = mergesort(case[0])
            assert res == case[1]
            print(
                f"PASS! Test #{i} passed. Input: {case[0]}, expected: {case[1]}, got: {res}"
            )
        except BaseException as e:
            print(
                f"FAIL! Test #{i} did not pass. Input: {case[0]}, expected: {case[1]}, got: {res}"
            )
