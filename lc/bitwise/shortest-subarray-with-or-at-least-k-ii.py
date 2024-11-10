class Solution:
    def remove(self, hs, num):
        total = 0
        t = 0
        for i in range(32):
            hs[i] -= 1 if ((num >> i) & 1) else 0
            if hs[i]:
                total += 2 ** t
            t+=1
        return total

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # bitwise & sliding window
        # time O(n), space O(1)
        n = len(nums)
        min_sub = n + 1
        i = 0
        cur = 0
        hs = [0] * 32
        for j in range(n):
            cur |= nums[j]
            for t in range(32):
                hs[t] += 1 if (nums[j] >> t) & 1 else 0
            # shrink i
            while cur >= k and i <= j:
                # remove nums[i] from hs
                cur = self.remove(hs, nums[i])
                min_sub = min(min_sub, j-i+1)
                i+=1
        return min_sub if min_sub < n+1 else -1
