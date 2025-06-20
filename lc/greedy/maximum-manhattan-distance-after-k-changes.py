class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # greedy
        # time O(n), space O(1)
        freq = defaultdict(int)
        res = 0
        for i,ch in enumerate(s):
            freq[ch] += 1
            diff = abs(freq['N'] - freq['S']) + abs(freq['W'] - freq['E'])
            res = max(res, diff + min(2*k, i+1-diff))
        return res