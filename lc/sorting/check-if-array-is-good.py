class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # sorting
        # time O(n), space O(n)
        n = len(nums)
        mark = [0] * n
        for num in nums:
            if num > n - 1 or num < 1:
                return False
            mark[num] += 1
            if num != n - 1 and mark[num] > 1:
                return False

        return mark[n - 1] == 2


class Solution1:
    def isGood(self, nums: List[int]) -> bool:
        # sorting
        # time O(nlogn), space O(1)
        n = len(nums)
        nums.sort()
        if nums[-1] != n - 1:
            return False
        for i in range(1, n):
            if nums[i - 1] != i:
                return False
        return True
