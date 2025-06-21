class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # counter
        # time O(n), space O(1) 
        freq = Counter(word)
        res = sys.maxsize
        for k1,v1 in freq.items():
            cnt = 0
            for k2, v2 in freq.items():
                if k1 == k2: continue
                if v2 < v1: 
                    cnt += v2
                elif v2 > v1 + k:
                    cnt += v2 - (v1 + k)

            res = min(res, cnt)
        return res