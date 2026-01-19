from typing import Callable, Sequence, Optional

# ============================================================
# 1) MINIMIZE k: smallest k such that condition(k) is True
#    Requires: condition is False...False, then True...True
# ============================================================
def binary_search_min_k(left: int, right: int, condition: Callable[[int], bool]) -> int:
    """
    Returns the smallest k in [left, right] with condition(k) == True.
    Assumes such k exists (i.e., condition(right) is True).
    """
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

# ============================================================
# 2) MAXIMIZE k: largest k such that condition(k) is True
#    Requires: True...True, then False...False (or equivalent)
# ============================================================
def binary_search_max_k(left: int, right: int, condition: Callable[[int], bool]) -> int:
    """
    Returns the largest k in [left, right] with condition(k) == True.
    Assumes such k exists (i.e., condition(left) is True).
    """
    while left < right:
        mid = left + (right - left + 1) // 2  # bias right
        if condition(mid):
            left = mid
        else:
            right = mid - 1
    return left

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
