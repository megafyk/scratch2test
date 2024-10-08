class Solution:
    def backtrack(self, candidates, target, ans, comb, start):
        if target == 0:
            ans.append(list(comb))
            return
        if target < 0 or len(comb) == len(candidates):
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            if i > start and candidates[i] == candidates[i-1]:
                # each comb appeared once
                continue 
            comb.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], ans, comb, i+1)
            comb.pop()             
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # complexity: time O(2^n), mem O(n)
        candidates.sort()
        ans = []
        self.backtrack(candidates, target, ans, [], 0)
        return ans
# from typing import List
#
#
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         ans = []
#         candidates.sort()
#
#         def helper(res, remain, start):
#             if remain == 0:
#                 ans.append(list(res))
#                 return
#             if remain < 0 or len(res) == len(candidates):
#                 return
#
#             for i in range(start, len(candidates)):
#                 if i > start and candidates[i] == candidates[i - 1]:
#                     continue  # use each number in candidates once
#                 res.append(candidates[i])
#                 helper(res, remain - candidates[i], i + 1)
#                 res.pop()
#
#         helper([], target, 0)
#         return ans
#
#
# s = Solution()
# print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
