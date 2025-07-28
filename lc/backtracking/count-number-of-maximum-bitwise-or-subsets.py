class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        for num in nums:
            best |= num
            
        @cache
        def dfs(cur, idx):
            if idx >= n:
                return 1 if cur == best else 0
            return dfs(cur | nums[idx], idx + 1) + dfs(cur, idx + 1)
        return dfs(0, 0)

class Solution1:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        n = len(nums)

        def backtrack(idx, cur_or):
            if idx >= n:
                return
            cnt[cur_or | nums[idx]] += 1
            backtrack(idx + 1, cur_or | nums[idx])
            backtrack(idx + 1, cur_or)

        backtrack(0, 0)
        return max(cnt.values())

class Solution2:
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