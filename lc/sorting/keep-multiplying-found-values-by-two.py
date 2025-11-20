class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # time O(n), space O(1)
        s = set(nums)
        for num in nums:
            if original in s:
                original <<= 1
        return original

class Solution1:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        n = len(nums)
        def search(num, l, r):
            while l <= r: # include mid
                mid = l + (r - l) // 2
                if nums[mid] == num:
                    return mid
                elif nums[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        start = 0
        while True:
            start = search(original, start, n-1)
            if start == -1:
                return original
            original *= 2
            
        return -1
