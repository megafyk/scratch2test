class Solution:
    def count_pair_(self, nums, k, mid):
        # count number of pair <= mid
        left = 0
        count = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left
        return count >= k

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # complexity: time O(nlogn + maxdislogn), mem O(1)
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if self.helper(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return left
