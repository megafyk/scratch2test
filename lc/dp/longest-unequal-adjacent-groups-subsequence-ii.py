class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        # dp longest incresing subsequence LIS
        # time O(n^2), space O(n^2)
        n = len(words)
        dp = [[i] for i in range(n)]

        mx = 1

        def ham(w1, w2):
            if len(w1) != len(w2):
                return 0
            cnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    cnt += 1
            return cnt

        for i in range(1, n):
            for j in range(0, i):
                if groups[j] != groups[i] and ham(words[j], words[i]) == 1:
                    if len(dp[i]) < len(dp[j]) + 1:
                        dp[i] = list(dp[j])
                        dp[i].append(i)

                        mx = max(mx, len(dp[i]))

        for i in range(n):
            if len(dp[i]) == mx:
                return [words[dp[i][j]] for j in range(mx)]
        return []
