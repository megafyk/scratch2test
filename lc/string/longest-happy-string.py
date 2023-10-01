class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        def dfs(lg, md, sm, lg_c, md_c, sm_c) -> str:
            # swap until lg >= md > sm
            if lg < md:
                return dfs(md, lg, sm, md_c, lg_c, sm_c)
            if md < sm:
                return dfs(lg, sm, md, lg_c, sm_c, md_c)
            if md == 0:
                return lg_c * min(2, lg)

            use_lg = min(2, lg)
            use_md = 1 if lg - use_lg >= md else 0

            return str(lg_c * use_lg) + str(md_c * use_md) + dfs(lg - use_lg, md - use_md, sm, lg_c, md_c, sm_c)

        return dfs(a, b, c, 'a', 'b', 'c')


s = Solution()
print(s.longestDiverseString(1, 1, 7))
print(s.longestDiverseString(2, 4, 1))
