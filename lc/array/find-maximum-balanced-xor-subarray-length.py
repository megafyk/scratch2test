class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        # prefix sum + hashtable
        # time O(n), space O(n)
        n = len(nums)
        diff = 0
        xor = 0
        first_xor_diff = defaultdict(int)
        first_xor_diff[(0, 0)] = -1
        res = 0
        for i in range(n):
            diff += 1 if nums[i] & 1 else -1
            xor ^= nums[i]
            if (xor, diff) in first_xor_diff:
                res = max(res, i - first_xor_diff[(xor, diff)])
            else:
                first_xor_diff[(xor, diff)] = i
        return res
