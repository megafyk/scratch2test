class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # two pointers
        # time O(n), space O(n)
        res = [-1]
        n = len(nums)
        for i, num in enumerate(nums):
            if num == key:
                res += [j for j in range(max(res[-1] + 1, 0, i - k), i)]
                res += [j for j in range(max(res[-1] + 1, i), min(i+k+1, n))]
        return res[1:]
