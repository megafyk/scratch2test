from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # string hashtable couting
        # time O(l), space O(1)
        if k > len(s): return False
        cnt = Counter(s)
        even = 0
        odd = 0
        for _,v in cnt.items():
            if v % 2:
                odd += 1
            else:
                even += 1

        k -= odd
        if k < 0: return False
        return True
