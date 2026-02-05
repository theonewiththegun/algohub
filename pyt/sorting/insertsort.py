from typing import TypeVar

from loguru import logger

T = TypeVar("T")


def insertion_sort(l: list[T]):
    for i in range(1, len(l)):
        curr = l[i]
        j = i - 1
        while j >= 0 and curr < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = curr
    return l


if __name__ == "__main__":
    print(insertion_sort([3, 1, 2]))
