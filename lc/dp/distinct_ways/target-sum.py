class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
        sum_to_find = (total + target) // 2
        
        dp = [0] * (sum_to_find + 1)
        dp[0] = 1  # Base case: one way to make sum 0 (empty subset)
        
        for num in nums:
            for j in range(sum_to_find, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[sum_to_find]

class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # bottom up
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            nw_dp = defaultdict(int)
            for t in dp.keys():
                nw_dp[t+num] += dp[t]
                nw_dp[t-num] += dp[t]
            dp = nw_dp
        return dp[target]
        
class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # topdown
        n = len(nums)
        
        @cache
        def dfs(idx, target):
            if idx == n:
                return 1 if target == 0 else 0
            return dfs(idx + 1, target - nums[idx]) + dfs(idx + 1, target + nums[idx])

        return dfs(0, target)
