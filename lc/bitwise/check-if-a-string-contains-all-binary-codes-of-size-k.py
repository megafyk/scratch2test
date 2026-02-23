class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # bitwise
        # n = len(s)
        # time O(n), space O(1)
        k_set = set()
        cur = 0 
        mask = (1 << k) - 1
        for i in range(len(s)):
            cur <<= 1
            cur |= 1 if s[i] == "1" else 0
            cur &= mask # cut length = k
            if i >= k-1:
                k_set.add(cur)

        return len(k_set) == (mask+1)