class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # time O(nlog(n)), space O(1)
        banned = sorted(banned)
        i = 0
        cur_sum = 0
        res = 0
        for num in range(1, n+1):
            if num != banned[i]:
                if cur_sum + num > maxSum: return res
                cur_sum += num
                res += 1
            while i < len(banned) - 1 and banned[i] <= num:
                i += 1
        return res

    # def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
    #     # time O(N), space O(N)
    #     s = set(banned)
    #     res = 0
    #     cur_sum = 0
    #     for num in range(1, n+1):
    #         if num not in s:
    #             if cur_sum + num > maxSum:
    #                 return res
    #             cur_sum += num
    #             res += 1
    #     return res
