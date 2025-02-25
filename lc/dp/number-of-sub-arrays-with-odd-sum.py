class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # dp array
        # time O(n), space O(1)
        res = 0
        prev = [0,0]
        mod = 10 ** 9 + 7
        for i in range(len(arr)):
            if arr[i] % 2:
               prev[0], prev[1] = prev[1], prev[0]
            if arr[i] % 2 == 0:
                prev[0] += 1
            else:
                prev[1] += 1
            res += prev[1]
        return res % mod