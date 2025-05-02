class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search with condition
        # time O(logN), space O(1)
        N = len(nums)
        left, right = 0, N-1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1 # default
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1 # defaut
        return -1
