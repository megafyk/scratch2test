class Solution:
    def dfs(self,res,arr, k, n, fr):
        if len(arr) == k:
            res.append(list(arr))
            return
        
        for i in range(fr, n+1):
            arr.append(i)
            self.dfs(res, arr, k, n, i+1)
            arr.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(res, [], k, n, 1)
        return res


# from typing import List


# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         ans = []

#         def helper(res: List[int], from_num: int):
#             if len(res) == k:
#                 ans.append(list(res))
#                 return

#             for num in range(from_num, n + 1):
#                 res.append(num)
#                 helper(res, num + 1)
#                 res.pop()

#         helper([], 1)

#         return ans


# s = Solution()
# print(s.combine(4, 2))
