class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # time O(n), space O(n)
        n = len(nums)
        mi = n
        target = sum(nums) % p
        if target == 0: return 0
        prefix_mod = {0: -1}
        prefix = 0
        for idx, num in enumerate(nums):
            prefix = (prefix + num) % p
            need = (prefix - target + p) % p
            if need in prefix_mod:
                mi = min(mi, idx - prefix_mod[need])
            prefix_mod[prefix] = idx
        return mi if mi < n else -1
                
