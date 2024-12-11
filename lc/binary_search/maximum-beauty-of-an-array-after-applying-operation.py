class Solution:

    def max_sub_arr(self, nums, k, j):
        l, r = 0, j
        while l < r:
            mid = l + (r - l) // 2
            if nums[j] - nums[mid] <= 2 * k:
                r = mid
            else:
                l = mid + 1
        return j - l + 1

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # binary search + sorting
        # time O(nlogn), space O(1)
        nums = sorted(nums)
        mx = 1
        for j in range(len(nums)-1, 0, -1):
            mx = max(mx, self.max_sub_arr(nums, k, j))
        return mx
