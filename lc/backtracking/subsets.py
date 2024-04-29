class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

    # def dfs(self, res, arr, nums, used):
    #     res.append(list(arr))
    #     for i in range(len(nums)):
    #         if nums[i] in used:
    #             continue
            
    #         used.add(nums[i])
    #         arr.append(nums[i])

    #         self.dfs(res, arr, nums[i:], used)
            
    #         arr.pop()
    #         used.remove(nums[i])

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     used = set()
    #     self.dfs(res, [], nums, used)
    #     return res

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) == 0:
    #         return [[]]

    #     ans = [[]]

    #     for i in range(len(nums)):
    #         tmp_set = [nums[i]]
    #         smaller_nums = nums[i + 1 :]

    #         for sub in self.subsets(smaller_nums):
    #             ans.append(tmp_set + sub)

    #     return ans