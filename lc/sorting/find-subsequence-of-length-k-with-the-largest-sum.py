class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # sorting
        # time O(nlogn), space O(n)
        arr = [(num,i) for i,num in enumerate(nums)]
        arr = sorted(arr, reverse=True)[:k]
        arr = sorted(arr, key=lambda x: x[1])
        return [num for num,_ in arr]