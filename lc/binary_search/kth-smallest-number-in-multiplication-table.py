class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def enough(mid: int) -> bool:
            count = 0
            for row in range(1, m+1):
                num_small = min(mid // row, n)
                if num_small == 0:
                    break
                count += num_small
            return count >= k

        left, right = 1, m*n
        while left < right:
            mid = left + (right - left)//2
            if enough(mid):
                right = mid
            else:
                left = mid + 1

        return left


s = Solution()
print(s.findKthNumber(3, 3, 5))
