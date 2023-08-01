"""
"""
import time
from datetime import timedelta

recur_calls = 0


def binary_search_iter(_list, n):
    first_idx = 0
    last_idx = len(_list) - 1
    while last_idx >= first_idx:
        mid_idx = (first_idx + last_idx) // 2
        if _list[mid_idx] == n:
            return True
        else:
            if n < _list[mid_idx]:
                last_idx = mid_idx - 1
            else:
                first_idx = mid_idx + 1
    return False


def binary_search_recur(_list, n, first=0, last=None):
    if last is None:
        last = len(_list) - 1
    if last < first:
        return False
    mid = (first + last) // 2
    if _list[mid] == n:
        return True
    if n < _list[mid]:
        last = mid - 1
    else:
        first = mid + 1
    return binary_search_recur(_list, n, first, last)


if __name__ == "__main__":
    _list = list(range(20_000_000))

    not_in_list = binary_search_recur(_list, 100_000_000)

    is_in_list = binary_search_recur(_list, 5)
    print(f"not_in_list = {not_in_list} ", end="")
    print("is_in_list = {is_in_list}")
