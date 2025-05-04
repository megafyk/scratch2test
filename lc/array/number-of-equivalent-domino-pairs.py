class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # hashmap
        # time O(n), space O(1)
        res = 0
        p = defaultdict(int)
        for a,b in dominoes:
            k = a * 10 + b if a > b else b * 10 + a
            res += p[k]
            p[k] += 1
        return res