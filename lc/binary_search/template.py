from typing import Callable, Sequence, Optional

# ============================================================
# 1) MINIMIZE k: smallest k such that condition(k) is True
#    Requires: condition is False...False, then True...True
# ============================================================
def binary_search_min_k(left: int, right: int, condition: Callable[[int], bool]) -> int:
    """
    Returns the smallest k in [left, right] with condition(k) == True,
    or -1 if no such k exists.
    """
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if condition(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

# ============================================================
# 2) MAXIMIZE k: largest k such that condition(k) is True
#    Requires: True...True, then False...False (or equivalent)
# ============================================================
def binary_search_max_k(left: int, right: int, condition: Callable[[int], bool]) -> int:
    """
    Returns the largest k in [left, right] with condition(k) == True,
    or -1 if no such k exists.
    """
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if condition(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

# ============================================================
# 3) CLASSIC: find target index in sorted array
# ============================================================
def binary_search_if_exists(array: Sequence[int], target: int) -> int:
    if not array:
        return -1
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
