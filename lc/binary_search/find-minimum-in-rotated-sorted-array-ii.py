class Solution
    def findMin(self, arr: List[int]) -> int:
        # binary search
        # time O(n), space O(1)
        l,r = 0, len(arr) - 1
        while l < r:
            mid = l + (r-l) // 2
            if arr[mid] > arr[r]:
                l = mid + 1
            elif arr[mid] < arr[r]:
                r = mid
            else:
                r -= 1
        return arr[l]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # time O(logn), space O(n)
        s = set()
        arr = []
        for num in nums:
            if num not in s:
                s.add(num)
                arr.append(num)

        l,r = 0, len(arr) - 1
        while l < r:
            mid = l + (r-l) // 2
            if arr[mid] > arr[-1]:
                l = mid + 1
            else:
                r = mid
        return arr[l]
