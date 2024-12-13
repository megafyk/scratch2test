class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # dp kadane's algorithm
        # time O(n), space O(1)
        mod = 10 ** 9 + 7
        mx = max(0, arr[0])
        n = len(arr)

        prev = arr[0]
        total = arr[0]

        for i in range(1, n):
            prev = max(arr[i], prev + arr[i])
            mx = max(mx, prev)
            total += arr[i]

        if k == 1:
            return mx

        mx1 = 0
        for i in range(n):
            prev = max(arr[i], prev + arr[i])
            mx1 = max(mx1, prev)
        if total > 0:
            mx = max(mx, total * k, mx1 + (k-2) * total)
        else:
            mx = max(mx, total * k, mx1)
        return mx % mod
