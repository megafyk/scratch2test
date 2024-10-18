class Solution:
    def backtrack(self, nums, target, i, cur_or, cur):
        count = 0
        if cur_or == target:
            count += 1
        for j in range(i+1, len(nums)):
            cur.append(nums[j])
            count += self.backtrack(nums, target, j, cur_or | nums[j], cur)
            cur.pop()
        return count
        
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # backtrack
        # time O(2^n), space O(n)
        target = 0
        for num in nums:
            target |= num
        return self.backtrack(nums, target, -1, 0, [])