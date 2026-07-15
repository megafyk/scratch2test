class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # hashtable
        # time O(n), space O(n)
        cnt_0 = cnt_1 = 0
        res = 0
        first = defaultdict(int)
        n = len(nums)
        for i in range(n):
            if nums[i]: cnt_1 += 1
            else: cnt_0 += 1
            if cnt_1 == cnt_0:
                res = max(res, i+1)
            else:
                diff = cnt_1 - cnt_0
                if diff in first:
                    res = max(res, i - first[diff])
                else:
                    first[diff] = i
        return res
