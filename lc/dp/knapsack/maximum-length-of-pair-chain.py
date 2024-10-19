class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # greedy
        # time O(n), space O(1)
        pairs = sorted(pairs, key=lambda x: x[1])
        chain = 1
        prev = pairs[0]
        for i in range(1, len(pairs)):
            if pairs[i][0] > prev[1]:
                chain += 1
                prev = pairs[i]
        return chain

    # def findLongestChain(self, pairs: List[List[int]]) -> int:
    #     # knapsack bottom up
    #     # time O(n^2), space O(n)
    #     n = len(pairs)
    #     pairs = sorted(pairs)
    #     dp = [1] * n
    #     for i in range(1, n):
    #         for j in range(i):
    #             if pairs[i][0] > pairs[j][1]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
        
    #     return dp[-1]
        
    # def dp(self, pairs, i, j, memo):
    #     if j == len(pairs): return 0
    #     if (i,j) in memo: return memo[(i,j)]
    #     take = 0
    #     if i == -1 or pairs[i][1] < pairs[j][0]:
    #         take = 1 + self.dp(pairs, j, j+1, memo)
    #     not_take = self.dp(pairs, i, j+1, memo)
    #     memo[(i, j)] = max(take, not_take)
    #     return memo[(i, j)]

    # def findLongestChain(self, pairs: List[List[int]]) -> int:
    #     # knapsack top down
    #     # time O(n^2), space O(n)
    #     memo = {}
    #     pairs = sorted(pairs, key=cmp_to_key(self.cmp))
    #     return self.dp(pairs, -1, 0, memo)
        
        