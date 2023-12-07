from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(res: List[int], from_num: int):
            if len(res) == k:
                ans.append(list(res))
                return

            for num in range(from_num, n + 1):
                res.append(num)
                helper(res, num + 1)
                res.pop()

        helper([], 1)

        return ans


s = Solution()
print(s.combine(4, 2))
