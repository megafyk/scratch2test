class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        adj = defaultdict(list)
        for allow in allowed:
            adj[allow[:2]].append(allow[-1])
            
        @cache
        def bottoms(i, bot):
            # n = len(bot) => time O(n ^ n)
            if i >= len(bot) - 2:
                if i == len(bot) - 2:
                    return adj[bot[i] + bot[i+1]]
                return []
            u = bot[i] + bot[i+1]
            res = []
            for v in adj[u]:
                for suffix in bottoms(i+1, bot):
                    res.append(v + suffix)
            return res

        @cache
        def check(bot):
            if len(bot) == 1:
                return True

            bottom_list = bottoms(0, bot)
            for b in bottom_list:
                if check(b):
                    return True
            return False

        return check(bottom)
