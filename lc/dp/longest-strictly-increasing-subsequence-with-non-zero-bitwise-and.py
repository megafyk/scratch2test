class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # dp lis + optimize by patience sorting
        # n = len(nums)
        # time O(32*nlogn), space O(n)
        tails = [[] for _ in range(32)]
        max_length = 0
        for i in range(32):
            for num in nums:
                if (num >> i) & 1:
                    idx = bisect.bisect_left(tails[i], num)
                    if idx == len(tails[i]):
                        tails[i].append(num)
                    else:
                        tails[i][idx] = num
        for i in range(32):
            max_length = max(max_length, len(tails[i]))
        return max_length
