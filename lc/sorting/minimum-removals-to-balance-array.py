class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # sorting + sliding window
        # time O(nlogn), space O(1)
        n = len(nums)
        nums.sort()
        mx_win = 0
        l = 0
        for r in range(n):
            while l <= r and nums[l] * k < nums[r]:
                l += 1
            mx_win = max(mx_win, (r-l+1))
        return n - mx_win

        