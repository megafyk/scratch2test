class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words)

        start_with = defaultdict(list)
        end_with = defaultdict(list)
        for w in words:
            start_with[w[0]].append(w)
            end_with[w[-1]].append(w)
        res = []
        for i in range(n):
            for j in range(n):
                if i != j:

                    top = words[i]
                    bot = words[j]

                    top_cand_left = [v for v in start_with[top[0]]]
                    top_cand_right = [v for v in start_with[top[3]]]
                    bot_cand_left = [v for v in end_with[bot[0]]]
                    bot_cand_right = [v for v in end_with[bot[3]]]
                    left = []
                    right = []
                    for tl in top_cand_left:
                        for bl in bot_cand_left:
                            if tl == bl and tl != top and tl != bot:
                                left.append(tl)

                    for tr in top_cand_right:
                        for br in bot_cand_right:
                            if tr == br and tr != top and tr != bot:
                                right.append(tr)

                    for l in left:
                        for r in right:
                            if l != r:
                                res.append([top,l,r,bot])
        res.sort()
        return res