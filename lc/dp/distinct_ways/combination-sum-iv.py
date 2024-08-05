class Solution:
    def dp(self, nums, target, memo):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target in memo:
            return memo[target]
        ans = 0
        for i in range(len(nums)):
            if nums[i] > target:
                break
            ans += self.dp(nums, target - nums[i], memo)
        memo[target] = ans
        return ans

    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp distinct ways
        # complexity: time O(n*target), mem O(target)
        nums.sort()  # optimize run time
        return self.dp(nums, target, {})
