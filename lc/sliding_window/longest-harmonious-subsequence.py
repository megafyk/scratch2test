class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # hashtable
        # time O(n), space O(n)
        freq = Counter(nums)

        res = 0
        for k, v in freq.items():
            if (k + 1) in freq:
                res = max(res, v + freq[k + 1])
            if (k - 1) in freq:
                res = max(res, v + freq[k - 1])
        return res
