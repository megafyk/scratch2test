class Solution:
    def maximizeSquareArea(self, m: int, n: int, hs: List[int], vs: List[int]) -> int:
        # sorting
        # time O(m^2 + n^2), space O(1)
        mod = 10 ** 9 + 7

        def find_diff(arr, b):
            arr.append(1)
            arr.append(b)
            arr.sort()
            s_diff = set()
            for i in range(len(arr)-1):
                for j in range(i+1, len(arr)):
                    s_diff.add(arr[j] - arr[i])
            return s_diff
        res = 0
        
        h_diff = find_diff(hs, m)
        v_diff = find_diff(vs, n)

        for a in h_diff:
            if a in v_diff:
                res = max(res, a * a)
        return res % mod if res != 0 else -1

