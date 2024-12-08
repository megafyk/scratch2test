class Solution:
    def cost(self, w1, w2):
        m = len(w1)
        n = len(w2)
        cost = n
        for i in range(m):
            sub_w1 = w1[i:]
            if w2.startswith(sub_w1):
                cost = n - (m - i)
                break
        return cost

    def shortestSuperstring(self, words: List[str]) -> str:
        # dp travelling salesman problem
        # time O(n^2 + 2^n), space O(n^2 + 2^n)
        n = len(words)
        graph = [[0] * n for _ in range(n)] # cost i -> j
        for i in range(n):
            for j in range(n):
                graph[i][j] = self.cost(words[i], words[j])
                graph[j][i] = self.cost(words[j], words[i])


        end = (1 << n) - 1
        dp = [[(sys.maxsize, "")] * n for _ in range(end + 1)]
        lenres, res = sys.maxsize, ""
        for mask in range(end + 1):
            for j in range(n):
                if mask & (1 << j) != 0:
                    premask = mask ^ (1 << j)  # previous
                    if premask == 0:
                        dp[mask][j] = len(words[j]), words[j]
                    else:
                        for k in range(n):
                            prelen, prestr = dp[premask][k]
                            curlen, curstr = dp[mask][j]
                            if prelen + graph[k][j] < curlen:
                                dp[mask][j] = (
                                    prelen + graph[k][j],
                                    prestr + words[j][-graph[k][j]:],
                                )
                if mask == end and dp[mask][j][0] < lenres:
                    lenres, res = dp[mask][j]
        return res
