class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # dp string
        # time O(n*2^n), space O(2^n)
        wordDict = set(wordDict)
        res = []

        n = len(s)

        def dp(i, cur):
            if i >= n:
                res.append(" ".join(cur))
                return

            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    cur.append(s[i:j+1])
                    dp(j+1, cur)
                    cur.pop()
        dp(0, [])
        return res
