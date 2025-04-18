class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search
        # time O(log(N-k)), space O(k)
        N = len(arr)
        left, right = 0, N-k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] <= arr[mid+k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left: left+k]
            