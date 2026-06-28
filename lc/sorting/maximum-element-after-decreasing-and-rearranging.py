class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # sorting
        # time O(nlogn), space O(1)
        arr.sort()
        prev = 1
        for i in range(1, len(arr)):
            if arr[i] > prev + 1:
                prev += 1
            else:
                prev = arr[i]
        return prev
