class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] -> lcs A[i:] vs B[j:]
        # time O(m*n), space O(1)
        m = len(nums1)
        n = len(nums2)
        dp = [0] * (n+1)
        mx = 0
        for i in range(1, m+1):
            dp2 = [0] * (n+1)
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp2[j] = dp[j-1] + 1
                    mx = max(mx, dp2[j])
            dp = dp2
        return mx
