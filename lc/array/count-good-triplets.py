class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # brute force
        # time O(N^3), space O(1)
        res = 0
        n = len(arr)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[k] - arr[i]) <= c:
                        res += 1
        return res 