class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # knapsack
        # time O(n), space O(n)
        cnt = {}
        s = set()
        for num in nums:
            if num not in cnt:
                cnt[num] = 0
            cnt[num] += 1
            s.add(num)
        nums = sorted(list(s))
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = cnt[nums[0]] * nums[0]
        for i in range(2, n+1):
            if nums[i-1] == nums[i-2] + 1:
                dp[i] = max(dp[i-1], nums[i-1] * cnt[nums[i-1]] + dp[i-2])
            else:
                dp[i] = dp[i-1] + nums[i-1] * cnt[nums[i-1]]
        return dp[-1]
