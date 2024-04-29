class Solution:


    def dfs(self, res, arr, nums, used):
        n = len(nums)
        if len(arr) == n:
            res.append(list(arr)) # shallow copy
            return res

        for num in nums:
            if num in used:
                continue
            used.add(num)
            arr.append(num)
            self.dfs(res, arr, nums, used)
            arr.pop()
            used.remove(num)
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        self.dfs(res, [], nums, used)
        return res


    # def permute(self, nums: List[int]) -> List[List[int]]:
        # if len(nums) == 0:
        #     return [[]]
        # if len(nums) == 1:
        #     return [nums]
        # ans = []
        # for i in range(len(nums)):
        #     detach_n = nums[i]
        #     smaller_nums = nums[:i] + nums[i+1:]
            
        #     for p in self.permute(smaller_nums):
        #         ans.append([detach_n] + p)

        # return ans