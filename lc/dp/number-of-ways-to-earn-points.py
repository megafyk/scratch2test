class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # knapsack 0/1 bottom up + space optimize
        # time O(n*target*cnt), space O(n*target)
        mod = 10**9 + 7
        n = len(types)

        dp = [0] * (target + 1)  # dp[i] # ways earn j use
        dp[0] = 1
        for i in range(1, n + 1):
            nw_dp = [0] * (target + 1)
            cnt, mark = types[i - 1]
            for j in range(target + 1):
                for k in range(cnt + 1):
                    if k * mark <= j:
                        nw_dp[j] = (nw_dp[j] + dp[j - k * mark]) % mod
            dp = nw_dp
        return dp[-1]


class Solution1:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # knapsack 0/1 bottom up
        # time O(n*target*cnt), space O(n*target)
        mod = 10**9 + 7
        n = len(types)

        dp = [
            [0] * (target + 1) for _ in range(n + 1)
        ]  # dp[i][j] => # ways earn j use i quest
        dp[0][0] = 1
        for i in range(1, n + 1):
            cnt, mark = types[i - 1]
            for j in range(target + 1):
                for k in range(cnt + 1):
                    if k * mark <= j:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - k * mark]) % mod
        return dp[-1][-1]


class Solution2:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # knapsack 0/1 top down
        # time O(n*target*cnt), space O(n*target)
        n = len(types)
        mod = 10**9 + 7

        @cache
        def dfs(cur, idx):
            if idx == n:
                return 1 if cur == target else 0
            cnt, mark = types[idx]
            res = 0
            for k in range(cnt + 1):
                earn = cur + k * mark
                if earn <= target:
                    res = (res + dfs(earn, idx + 1)) % mod
            return res

        return dfs(0, 0)
