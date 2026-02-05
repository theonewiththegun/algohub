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
