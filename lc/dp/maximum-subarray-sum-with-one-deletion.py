class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # dp + kadane's algorithm -> find max sum sub arr
        # time O(n), space O(n)
        n = len(arr)
        if n == 1: return arr[0]
        dp_l = list(arr) # go from left
        dp_r = list(arr) # go from right
        for i in range(1, n):
            dp_l[i] = max(dp_l[i-1] + arr[i], arr[i])
            dp_r[n-i-1] = max(dp_r[n-i] + arr[n-i-1], arr[n-i-1])

        mx = arr[0]
        for i in range(n):
            if i == 0:
                mx = max(mx, dp_r[i], dp_r[i+1])
            elif i == n-1:
                mx = max(mx, dp_l[i], dp_l[i-1])
            else:
                mx = max(mx, dp_l[i-1] + dp_r[i+1], dp_l[i] + dp_r[i+1])
        return mx
