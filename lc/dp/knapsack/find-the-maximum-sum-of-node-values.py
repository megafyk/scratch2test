class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # dp 0/1 knapsack
        # time O(n), space O(n)
        n = len(nums)
        dp = [[0] * 2 for _ in range(n+1)] # dp[x][1] => xor node x, dp[x][0] => not xor node x
        dp[n][0] = -sys.maxsize
        dp[n][1] = 0
        
        for i in range(n-1,-1,-1):
            for j in range(2):
                xor = dp[i+1][j^1] + (nums[i] ^ k)
                not_xor = dp[i+1][j] + nums[i]
                dp[i][j] = max(xor, not_xor)
        return dp[0][1]

    
    # def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
    #     # greedy
    #     # time O(nlogn), space O(n)
    #     n = len(nums)
    #     total = sum(nums)
    #     delta = [((nums[i] ^ k) - nums[i]) for i in range(n)]
    #     delta = sorted(delta, reverse=True)
    #     for i in range(0, n, 2):
    #         if i == n - 1: break
    #         t = delta[i] + delta[i + 1]
    #         if t < 0: break
    #         total += t
    #     return total
