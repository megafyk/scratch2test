class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # complexity: time O(n), space O(n)
        res = []
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]
        for left, right in queries:
            if left == right:
                res.append(arr[left])
            else:
                res.append(prefix[right]^prefix[left-1] if left > 0 else prefix[right])   
        return res
