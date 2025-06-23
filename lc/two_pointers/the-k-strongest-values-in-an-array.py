class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # comlexity: time O(n), mem O(1)
        arr = sorted(arr)
        n = len(arr)
        l = 0
        h = n - 1
        m = arr[(n-1)//2]
        res = []

        while k > 0:
            if abs(arr[h]-m) >= abs(arr[l]-m):
                res.append(arr[h])
                h -= 1
            else:
                res.append(arr[l])
                l += 1
            k -= 1

        return res 