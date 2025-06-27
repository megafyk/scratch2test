class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # string + combinatoric + bfs
        # time O(n + 26^(n//k) * n + log(26^(n//k))), space O(n + 26^(n//k))
        def is_sub_seq(s, t):
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    j += 1
                i += 1
            return j == len(t)

        freq = Counter(s)
        n = len(s)
        allow_cnts = defaultdict(int)
        for c, cnt in freq.items():
            if cnt >= k:
                allow_cnts[c] = cnt // k

        cand = [] # sub sequence candidate
        # start with 1 char
        for c, cnt in allow_cnts.items():
            cnt = defaultdict(int)
            cnt[c] = 1
            cand.append((c, cnt))

        while True: # bfs
            new_cand = []
            for cur_sub, cnt in cand:
                for c, allow_cnt in allow_cnts.items():
                    if cnt[c] <= allow_cnt:
                        if is_sub_seq(s, (cur_sub + c) * k):
                            new_cnt = cnt.copy()
                            new_cnt[c] += 1
                            new_cand.append((cur_sub + c, new_cnt))
                
            if not new_cand: break
            cand = new_cand
        cand = sorted(cand, reverse=True)
        return cand[0][0] if cand else ""