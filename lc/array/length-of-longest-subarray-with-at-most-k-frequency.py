class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # hashmap
        # time O(n), space O(n)
        n = len(nums)
        cnt = defaultdict(int)
        i = 0
        res = 0
        for j in range(n):
            cnt[nums[j]] += 1
            while cnt[nums[j]] > k:
                cnt[nums[i]] -= 1
                i += 1
            res = max(res, j-i+1)
        return res
