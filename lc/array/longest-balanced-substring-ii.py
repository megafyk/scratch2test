class Solution:
    def longestBalanced(self, s: str) -> int:
        # prefix sum + hashtable
        # time O(n), space O(n)
        def cnt_one():
            res = 1
            cur = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    cur += 1
                    res = max(res, cur)
                else:
                    cur = 1
            return res

        def cnt_two(c1, c2):
            first = defaultdict(int)
            first[0] = -1
            cnt_c1 = 0
            res = 0
            for i in range(len(s)):
                if s[i] != c1 and s[i] != c2:
                    first = defaultdict(int)
                    first[0] = i
                    cnt_c1 = 0
                else:
                    cnt_c1 += 1 if s[i] == c1 else -1
                    if cnt_c1 in first:
                        res = max(res, i - first[cnt_c1])
                    else:
                        first[cnt_c1] = i
            return res

        def cnt_three():
            cnt = defaultdict(int)
            first = defaultdict(int)
            first[(0, 0)] = -1
            res = 0
            for i in range(len(s)):
                cnt[s[i]] += 1
                diff = (cnt["b"] - cnt["a"], cnt["c"] - cnt["a"])
                if diff in first:
                    res = max(res, i - first[diff])
                else:
                    first[diff] = i
            return res

        return max(
            cnt_one(),
            cnt_two("a", "b"),
            cnt_two("b", "c"),
            cnt_two("c", "a"),
            cnt_three(),
        )
