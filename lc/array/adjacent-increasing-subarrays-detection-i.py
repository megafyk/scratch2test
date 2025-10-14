class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        res = pre = cur = 0
        for i in range(n):
            if i > 0 and nums[i] > nums[i-1]:
                cur += 1
            else:
                pre = cur
                cur = 1
            res = max(res, cur//2, min(pre,cur))
            if res >= k: return True
        return False