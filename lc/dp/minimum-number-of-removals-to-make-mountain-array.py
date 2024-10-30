class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # dp lis
        # time O(n^2), space O(n)
        n = len(nums)
        lis = [1] * n # longest incresing subsequence
        lds = [1] * n # longest decresing subsequence

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        for i in range(n-2,-1, -1):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        min_rm = n

        for i in range(1, n-1):
            if lds[i] > 1 and lis[i] > 1:
                min_rm = min(min_rm, n-lis[i]-lds[i] + 1)
        return min_rm
