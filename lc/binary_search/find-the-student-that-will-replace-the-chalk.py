class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # binary search + prefixsum
        # complexity: time O(n), mem O(n)
        n = len(chalk)
        presum = [0] * n
        total = 0
        for i in range(n):
            total += chalk[i]
            presum[i] = total
        
        k %= total
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if presum[mid] > k:
                right = mid
            else:
                left = mid + 1
        return left
