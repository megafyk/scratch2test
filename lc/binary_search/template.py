# ===================================================================
# 1. MINIMIZE k → Find the smallest value where condition(k) is True
# ===================================================================
def binary_search_min_k(array) -> int:
    def condition(value) -> bool:
        pass
    """
    Use when: You want the SMALLEST k such that condition(k) == True
    Example: Minimum capacity to ship packages, minimum days, etc.
    """
    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid # move left to find smaller k
        else:
            left = mid + 1
    return left

# ===================================================================
# 2. MAXIMIZE k → Find the largest value where condition(k) is True
# ===================================================================
def binary_search_max_k(array) -> int:
    def condition(value) -> bool:
        pass
    """
    Use when: You want the LARGEST k such that condition(k) == True
    Example: Max eating speed, max length of subarray, etc.
    """
    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left + 1) // 2
        if condition(mid):
            left = mid # move right to find larger k
        else:
            right = mid - 1
    return left

# ===================================================================
# 3. CLASSIC: Find if target exists in sorted array
# ===================================================================
def binary_search_if_exists(array, num) -> int:
    """
    Standard search in sorted array → return index or -1
    """
    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left <= right: # because we include mid
        mid = left + (right - left) // 2
        if array[mid] == num:
            return mid
        elif array[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return -1