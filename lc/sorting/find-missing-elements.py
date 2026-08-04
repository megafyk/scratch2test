class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # sorting
        # time O(n), space O(n)
        s = set()
        mi,mx = inf, -inf
        for n in nums:
            s.add(n)
            mi = min(mi, n)
            mx = max(mx, n)
        res = []
        for n in range(mi+1, mx):
            if n not in s:
                res.append(n)
        return res
