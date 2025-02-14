class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # array
        # time O(n), space O(n)
        n = len(nums)
        diff = [0] * n
        for idx, num in enumerate(nums):
            diff[idx] = num - idx
        
        res = 0
        hm = defaultdict(int)
        
        for idx, n in enumerate(diff):
            res += (idx if n not in hm else idx - hm[n])
            hm[n] += 1
        return res