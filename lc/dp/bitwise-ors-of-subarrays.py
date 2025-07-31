class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # dp + bitmask
        # time O(32n), space O(n)
        or_sub_arr = set()
        res = set()
        for num in arr:
            or_sub_arr = {num | t for t in or_sub_arr}
            or_sub_arr.add(num)
            res |= or_sub_arr # union 2 set
        return len(res)

class Solution1:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # dp + bitmask
        # time O(32n), space O(n)
        or_sub_arr = set()
        res = set()
        for num in arr:
            new_or_sub_arr = set()
            for t in or_sub_arr:
                new_or_sub_arr.add(num | t)

            new_or_sub_arr.add(num)
            or_sub_arr = new_or_sub_arr

            for t in or_sub_arr:
                res.add(t)
        return len(res)