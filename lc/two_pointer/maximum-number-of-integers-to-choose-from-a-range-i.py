class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # time O(N), space O(N)
        s = set(banned)
        res = 0
        cur_sum = 0
        for num in range(1, n+1):
            if num not in s:
                if cur_sum + num > maxSum:
                    return res
                cur_sum += num
                res += 1
        return res
